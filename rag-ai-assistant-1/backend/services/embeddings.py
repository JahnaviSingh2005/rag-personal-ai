from sentence_transformers import SentenceTransformer

# Use ONE model everywhere
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_chunks(chunks):
    texts = [chunk["text"] for chunk in chunks]

    # Always return LIST OF LISTS (not numpy)
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings.tolist()
