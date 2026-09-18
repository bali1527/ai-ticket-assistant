import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.anomaly_detector import (
    get_unresolved_high_priority,
    get_resolution_time_anomalies,
    get_low_rated_tickets
)

print("\n=== Unresolved High/Critical Tickets ===")
print(get_unresolved_high_priority().head())

print("\nCount:")
print(len(get_unresolved_high_priority()))

print("\n=== Resolution Time Anomalies ===")
print(get_resolution_time_anomalies().head())

print("\nCount:")
print(len(get_resolution_time_anomalies()))

print("\n=== Low Rated Tickets ===")
print(get_low_rated_tickets().head())

print("\nCount:")
print(len(get_low_rated_tickets()))