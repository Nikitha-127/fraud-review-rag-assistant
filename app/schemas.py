from pydantic import BaseModel, Field
from typing import List, Optional


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, description="Fraud/compliance question to answer")
    top_k: int = Field(default=4, ge=1, le=10)


class SourceChunk(BaseModel):
    source: str
    content: str
    score: Optional[float] = None


class QueryResponse(BaseModel):
    answer: str
    sources: List[SourceChunk]


class IngestResponse(BaseModel):
    message: str
    chunks_indexed: int
