import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.query_engine import execute_query

query = """
SELECT agent_id,
       AVG(customer_rating) AS avg_rating
FROM tickets
WHERE customer_rating IS NOT NULL
GROUP BY agent_id
ORDER BY avg_rating ASC
LIMIT 1
"""

result = execute_query(query)

print(result)