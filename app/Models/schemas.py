from pydantic import BaseModel
from typing import Optional, List
from pydantic import Field


class Message(BaseModel):
    role: str  
    content: str


class ChatRequest(BaseModel):
    question: str
    history: List[Message] = Field(default_factory=list)
    session_id: Optional[str] = None
    doc_filter: Optional[str] = None  


class ChatResponse(BaseModel):
    answer: str
    sources: List[dict]
    token_usage: dict
    context_used: int


class DocumentUploadResponse(BaseModel):
    doc_id: str
    filename: str
    chunks_created: int
    status: str


class DocumentListResponse(BaseModel):
    documents: List[dict]