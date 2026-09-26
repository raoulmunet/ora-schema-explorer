from __future__ import annotations
import argparse,json
from .core import scan_path,render_html,render_markdown,render_mermaid

def main(argv=None):
    p=argparse.ArgumentParser(description="Explore Oracle schema source offline.")
    p.add_argument("source")
    p.add_argument("--format",choices=("markdown","json","mermaid","html"),default="markdown")
    a=p.parse_args(argv)
    m=scan_path(a.source)
    if a.format=="json": print(json.dumps(m.to_dict(),indent=2))
    elif a.format=="mermaid": print(render_mermaid(m))
    elif a.format=="html": print(render_html(m))
    else: print(render_markdown(m),end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
