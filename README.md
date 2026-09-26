# ora-schema-explorer

[![tests](https://github.com/raoulmunet/ora-schema-explorer/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-schema-explorer/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Build an offline, browsable overview of an Oracle schema from SQL/DDL files — **no database connection required**.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Common DDL and SQL dependency patterns |
> | Oracle Database 23ai | ✅ Common DDL and SQL dependency patterns |
> | Oracle AI Database 26ai | ✅ Common DDL and SQL dependency patterns |
>
> Unsupported release-specific syntax is not silently interpreted. This project documents only what the offline parsers can identify reliably.

## What it builds

From a folder containing `.sql` files, the tool collects:

- tables and columns;
- SQL objects read/written by scripts;
- a simple dependency graph;
- per-file summaries;
- Markdown, JSON, Mermaid or standalone HTML output.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-schema-explorer.git"

ora-schema-explorer examples/schema --format markdown > SCHEMA.md
ora-schema-explorer examples/schema --format mermaid > schema.mmd
ora-schema-explorer examples/schema --format html > schema.html
```

## Example workflow

A repository might contain:

```text
schema/
├── 01_customers.sql
├── 02_orders.sql
└── 10_load_customer_dim.sql
```

The generated overview then shows detected tables and SQL dependencies between source and target objects.

## Why offline?

It is useful for source repositories, code review, migration analysis, documentation generation and environments where database credentials should not be required.

## Limitations

Synonyms, dynamic SQL, editioning views, grants, runtime metadata and view expansion require a live database/catalog and are not guessed.

## Visual demo

A static visual preview is included in [`docs/index.html`](docs/index.html).

To publish it with GitHub Pages: **Settings → Pages → Deploy from a branch → `main` → `/docs`**. The repository is already prepared with `docs/.nojekyll`.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
