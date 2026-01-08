from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import sys
from pathlib import Path
from dotenv import load_dotenv
import os
import traceback

# Load environment variables from .env file (assuming it's in the root or backend root)
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

sys.path.insert(0, str(Path(__file__).parent.parent))

from api import upload, chat, health

app = FastAPI(title="RAG Personal AI Assistant")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"DEBUG: Middleware received request: {request.method} {request.url}", flush=True)
    try:
        response = call_next(request)
    except Exception as e:
        print(f"DEBUG: Middleware saw exception: {e}", flush=True)
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"detail": str(e)})
    return await response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"DEBUG: Global handler caught: {exc}", flush=True)
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "error": str(exc)},
    )

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(health.router, tags=["Health"])

@app.get("/")
def root():
    return {"message": "RAG Backend is running 🚀"}
