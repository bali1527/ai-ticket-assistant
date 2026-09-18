from fastapi import FastAPI
from pydantic import BaseModel

from app.llm_service import generate_sql
from app.query_engine import execute_query
from app.anomaly_detector import (
    get_unresolved_high_priority,
    get_resolution_time_anomalies,
    get_low_rated_tickets
)

app = FastAPI(
    title="AI Ticket Assistant"
)

class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/query")
def query_data(request: QueryRequest):

    sql = generate_sql(request.question)

    result = execute_query(sql)

    return {
        "question": request.question,
        "generated_sql": sql,
        "result": result.to_dict(orient="records")
    }


@app.get("/anomalies")
def anomalies():

    unresolved = get_unresolved_high_priority()

    resolution_anomalies = get_resolution_time_anomalies()

    low_rated = get_low_rated_tickets()

    return {
    "summary": {
        "unresolved_high_priority": len(unresolved),
        "resolution_time_anomalies": len(resolution_anomalies),
        "low_rated_tickets": len(low_rated)
    },
    "sample_records": {
        "unresolved": unresolved.head(5).to_dict(orient="records"),
        "resolution_anomalies": resolution_anomalies.head(5).to_dict(orient="records"),
        "low_rated": low_rated.head(5).to_dict(orient="records")
    }
}