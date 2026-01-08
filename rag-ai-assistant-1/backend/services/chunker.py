def chunk_text(text, metadata, chunk_size=500):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append({
            "text": chunk,
            "metadata": metadata
        })

    return chunks
