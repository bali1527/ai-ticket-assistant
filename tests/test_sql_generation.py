import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from app.llm_service import generate_sql
from app.query_engine import execute_query

question = "How many unresolved tickets are there?"

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)

result = execute_query(sql)

print("\nResult:")
print(result)