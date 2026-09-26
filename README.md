# ora-schema-explorer

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

## License

MIT.
