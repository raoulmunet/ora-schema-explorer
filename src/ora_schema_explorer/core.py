from __future__ import annotations
from dataclasses import dataclass,asdict
from pathlib import Path
from html import escape
import json
from ora_core import analyze_sql
from ora_doc import parse_tables

@dataclass(frozen=True)
class FileInfo:
    path:str
    tables:list[str]
    reads:list[str]
    writes:list[str]
    def to_dict(self): return asdict(self)

@dataclass(frozen=True)
class SchemaModel:
    files:list[FileInfo]
    tables:dict[str,list[dict]]
    edges:list[tuple[str,str]]
    def to_dict(self):
        return {"files":[f.to_dict() for f in self.files],"tables":self.tables,"edges":[list(e) for e in self.edges]}

def scan_path(path:str|Path)->SchemaModel:
    root=Path(path)
    files=[root] if root.is_file() else sorted(root.rglob("*.sql"))
    infos=[]; tables={}; edges=set()
    for f in files:
        sql=f.read_text(encoding="utf-8")
        parsed=parse_tables(sql)
        for t in parsed:
            tables[t.name]=[{"name":c.name,"datatype":c.datatype,"nullable":c.nullable} for c in t.columns]
        a=analyze_sql(sql)
        for r in a.read_objects:
            for w in a.write_objects:
                edges.add((r,w))
        infos.append(FileInfo(str(f),[t.name for t in parsed],a.read_objects,a.write_objects))
    return SchemaModel(infos,tables,sorted(edges))

def render_markdown(m:SchemaModel)->str:
    out=["# Oracle Schema Overview","",f"SQL files: {len(m.files)}",f"Detected tables: {len(m.tables)}",""]
    for name,cols in sorted(m.tables.items()):
        out += [f"## {name}","","| Column | Type | Nullable |","|---|---|---|"]
        out += [f"| {c['name']} | {c['datatype']} | {'Yes' if c['nullable'] else 'No'} |" for c in cols]
        out.append("")
    out += ["## Dependencies",""]
    out += [f"- `{a}` → `{b}`" for a,b in m.edges] or ["No read/write dependencies detected."]
    return "\n".join(out)+"\n"

def render_mermaid(m:SchemaModel)->str:
    lines=["flowchart LR"]; ids={}
    def node(x):
        if x not in ids: ids[x]=f"N{len(ids)}"
        return ids[x]
    for a,b in m.edges:
        lines.append(f'    {node(a)}["{a}"] --> {node(b)}["{b}"]')
    if not m.edges: lines.append('    N0["No dependencies detected"]')
    return "\n".join(lines)

def render_html(m:SchemaModel)->str:
    md=render_markdown(m)
    rows="".join(f"<li><code>{escape(a)}</code> &rarr; <code>{escape(b)}</code></li>" for a,b in m.edges)
    sections=[]
    for name,cols in sorted(m.tables.items()):
        tr="".join(f"<tr><td>{escape(c['name'])}</td><td>{escape(c['datatype'])}</td><td>{'Yes' if c['nullable'] else 'No'}</td></tr>" for c in cols)
        sections.append(f"<h2>{escape(name)}</h2><table><tr><th>Column</th><th>Type</th><th>Nullable</th></tr>{tr}</table>")
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Oracle Schema Explorer</title>
<style>body{{font-family:system-ui;max-width:1100px;margin:40px auto;padding:0 20px}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ccc;padding:6px;text-align:left}}code{{background:#f4f4f4;padding:2px 4px}}</style></head>
<body><h1>Oracle Schema Overview</h1><p>{len(m.files)} SQL files; {len(m.tables)} detected tables.</p>{''.join(sections)}
<h2>Dependencies</h2><ul>{rows or '<li>No dependencies detected.</li>'}</ul></body></html>"""
