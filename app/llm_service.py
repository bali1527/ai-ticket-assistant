from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SCHEMA = """
Table Name: tickets

Columns:

ticket_id
created_at

category

Possible category values:
Billing
Technical
General

priority

Possible priority values:
Low
Medium
High
Critical

status

Possible status values:
Open
Resolved
Escalated

response_time_hrs
resolution_time_hrs
agent_id
customer_rating
issue_summary
"""

def generate_sql(question: str):

    prompt = f"""
You are a SQLite expert.

Convert the user's question into a valid SQLite query.

Rules:
1. Return ONLY SQL.
2. No markdown.
3. No explanation.
4. Use exact column names.
5. Use exact values from the schema.
6. Use table name tickets.

Schema:
{SCHEMA}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()