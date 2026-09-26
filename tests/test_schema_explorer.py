from pathlib import Path
from ora_schema_explorer import scan_path,render_markdown

def test_scan(tmp_path:Path):
    (tmp_path/"a.sql").write_text("CREATE TABLE customers (customer_id NUMBER NOT NULL);",encoding="utf-8")
    (tmp_path/"b.sql").write_text("INSERT INTO dwh.customer_dim SELECT customer_id FROM customers;",encoding="utf-8")
    m=scan_path(tmp_path)
    assert "CUSTOMERS" in m.tables
    assert ("CUSTOMERS","DWH.CUSTOMER_DIM") in m.edges
    assert "Oracle Schema Overview" in render_markdown(m)
