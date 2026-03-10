from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag import ask_question

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    question: str
    answer: str


@router.post("/", response_model=ChatResponse)
def chat(body: ChatRequest):

    answer = ask_question(body.question)

    return {
        "question": body.question,
        "answer": answer
    }