import pdfplumber

from io import BytesIO

def load_document(file):
    chunks = []

    if file.filename.endswith(".pdf"):
        # Read file into memory to avoid SpooledTemporaryFile issues
        content = file.file.read()
        file_stream = BytesIO(content)
        
        with pdfplumber.open(file_stream) as pdf:
            for page_no, page in enumerate(pdf.pages):
                text = page.extract_text()

                if text and text.strip():
                    chunks.append({
                        "text": text,
                        "metadata": {
                            "filename": file.filename,
                            "page": page_no + 1
                        }
                    })

    return chunks
