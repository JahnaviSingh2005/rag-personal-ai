from fastapi import APIRouter, UploadFile, File, HTTPException
from services.document_loader import load_document
from services.chunker import chunk_text
from services.embeddings import embed_chunks
from services.vector_store import add_to_vector_store
import traceback

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    print(f"DEBUG: Endpoint hit. File: {file.filename}", flush=True)
    try:
        # 1. Load Document (extract text from pages)
        print("DEBUG: Starting load_document...", flush=True)
        raw_chunks = load_document(file)
        print(f"DEBUG: load_document done. Pages: {len(raw_chunks)}", flush=True)
        
        if not raw_chunks:
            raise HTTPException(status_code=400, detail="No text found in PDF")

        # 2. Chunk Text (split large pages into smaller chunks)
        print("DEBUG: Starting chunking...", flush=True)
        all_chunks = []
        for raw in raw_chunks:
            chunks = chunk_text(raw["text"], raw["metadata"])
            all_chunks.extend(chunks)
        print(f"DEBUG: Chunking done. Chunks: {len(all_chunks)}", flush=True)

        if not all_chunks:
             raise HTTPException(status_code=400, detail="Could not create chunks from text")

        # 3. Generate Embeddings
        print("DEBUG: Generating embeddings...", flush=True)
        embeddings = embed_chunks(all_chunks)
        print("DEBUG: Embeddings generated.", flush=True)

        # 4. Add to Vector Store
        print("DEBUG: Adding to vector store...", flush=True)
        add_to_vector_store(all_chunks, embeddings)
        print("DEBUG: Added to vector store.", flush=True)

        return {
            "message": "File processed and indexed successfully",
            "chunks_count": len(all_chunks),
            "filename": file.filename
        }

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
