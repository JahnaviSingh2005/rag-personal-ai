from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.rag_pipeline import run_rag

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

@router.post("/")
async def chat(request: ChatRequest):
    try:
        answer, sources = run_rag(request.query)
        return {
            "answer": answer,
            "sources": sources
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
