import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "tickets.db"

def execute_query(query: str):
    conn = sqlite3.connect(DB_PATH)

    try:
        df = pd.read_sql_query(query, conn)
        return df

    finally:
        conn.close()