import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = BASE_DIR / "data" / "support_tickets.csv"
db_path = BASE_DIR / "tickets.db"

print(f"Reading CSV from: {csv_path}")

df = pd.read_csv(csv_path)

print(f"Rows Loaded: {len(df)}")

df["created_at"] = pd.to_datetime(df["created_at"])

conn = sqlite3.connect(db_path)

df.to_sql(
    "tickets",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully!")
print(f"Database Location: {db_path}")