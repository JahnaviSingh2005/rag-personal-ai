
import sys
import os

# Mock the environment imports
sys.path.insert(0, os.path.abspath('backend'))

print("Step 1: Importing modules...", flush=True)
try:
    from services.document_loader import load_document
    from services.chunker import chunk_text
    from services.embeddings import embed_chunks
    from services.vector_store import add_to_vector_store
    print("Modules imported successfully.", flush=True)
except Exception as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

# Create a dummy PDF file content class to mock UploadFile
class MockFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'rb')

# Test with the debug PDF if it exists, or create a simple one
print("Step 2: Checking for test file...", flush=True)
test_file = "backend/debug.pdf"
if not os.path.exists(test_file):
    print(f"Test file {test_file} not found. Please provide a path or run in project root.")
    # Try to find any PDF in the dir
    files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    if files:
        test_file = files[0]
        print(f"Using {test_file} instead.")
    else:
        print("No PDF found for testing.")
        sys.exit(1)

print(f"Step 3: Loading document {test_file}...", flush=True)
try:
    mock_file = MockFile(test_file)
    raw_chunks = load_document(mock_file)
    print(f"Document loaded. Pages: {len(raw_chunks)}", flush=True)
except Exception as e:
    print(f"FAILED at load_document: {e}")
    sys.exit(1)

print("Step 4: Chunking text...", flush=True)
try:
    all_chunks = []
    for raw in raw_chunks:
        chunks = chunk_text(raw["text"], raw["metadata"])
        all_chunks.extend(chunks)
    print(f"Chunking done. Chunks: {len(all_chunks)}", flush=True)
except Exception as e:
    print(f"FAILED at chunk_text: {e}")
    sys.exit(1)

print("Step 5: Generating embeddings (This might be slow)...", flush=True)
try:
    embeddings = embed_chunks(all_chunks)
    print(f"Embeddings generated. Count: {len(embeddings)}", flush=True)
except Exception as e:
    print(f"FAILED at embed_chunks: {e}")
    sys.exit(1)

print("Step 6: Adding to vector store...", flush=True)
try:
    add_to_vector_store(all_chunks, embeddings)
    print("Added to vector store.", flush=True)
except Exception as e:
    print(f"FAILED at add_to_vector_store: {e}")
    sys.exit(1)

print("SUCCESS: Pipeline verification complete.")
