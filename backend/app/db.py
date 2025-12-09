import sqlite3
from typing import List, Dict

DB_PATH = "database.db"

def execute_sql(sql: str) -> List[Dict]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # make string comparisons case-insensitive
    conn.create_function("LOWER", 1, lambda s: s.lower() if isinstance(s, str) else s)

    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

