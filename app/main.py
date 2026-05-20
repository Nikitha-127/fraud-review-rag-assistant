# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel

from app.rag_service import query_rag

app = FastAPI(title="Fraud Review Assistant API")


class QueryRequest(BaseModel):
    question: str
    top_k: int = 4


@app.get("/")
def root():
    return {"message": "Fraud Review Assistant API Running"}


@app.post("/query")
def query_assistant(request: QueryRequest):
    return query_rag(
        request.question,
        request.top_k
    )
