from services.embeddings import model
from services.vector_store import search_vector_store
from services.llm import generate_answer

def run_rag(query):
    # 🔥 CRITICAL FIX: normalize + convert query embedding
    query_embedding = model.encode(
        query,
        convert_to_numpy=True,
        normalize_embeddings=True
    ).tolist()

    results = search_vector_store(query_embedding)

    docs = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not docs:
        return "Answer not found in the document.", []

    context = "\n".join(docs)
    answer = generate_answer(context, query)

    sources = [
        {
            "file": m.get("filename", "Unknown"),
            "page": m.get("page", "N/A")
        }
        for m in metadatas
    ]

    return answer, sources
