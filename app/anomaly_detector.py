import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "tickets.db"


def get_unresolved_high_priority():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT *
    FROM tickets
    WHERE priority IN ('High', 'Critical')
    AND status != 'Resolved'
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def get_resolution_time_anomalies():

    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql_query(
        "SELECT * FROM tickets WHERE resolution_time_hrs IS NOT NULL",
        conn
    )

    conn.close()

    mean = df["resolution_time_hrs"].mean()
    std = df["resolution_time_hrs"].std()

    threshold = mean + (2 * std)

    anomalies = df[
        df["resolution_time_hrs"] > threshold
    ]

    return anomalies


def get_low_rated_tickets():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT *
    FROM tickets
    WHERE customer_rating <= 2
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df