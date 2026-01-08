# 📚 Learning Resources: RAG Personal AI Assistant

This document lists the technologies used in this project and the best resources to learn them, from beginner to advanced.

---

## 1. 🐍 Core Language & Backend

### **Python**
The programming language used for the entire project.
- **Learn:** [Python for Beginners (Official)](https://www.python.org/about/gettingstarted/)
- **Practice:** [Real Python](https://realpython.com/) (Great tutorials)

### **FastAPI**
The framework used to build the Backend API (`backend/`). It's fast, modern, and easy to use.
- **Why we used it:** To handle file uploads and chat requests asynchronously.
- **Best Resource:** [FastAPI Official Documentation](https://fastapi.tiangolo.com/tutorial/) (It is considered one of the best documentations in the software world).

---

## 2. 🖥️ Frontend (UI)

### **Streamlit**
The library used to build the web interface (`frontend/`). It turns Python scripts into web apps.
- **Why we used it:** To create a UI for uploading files and chatting without writing HTML/CSS/JS.
- **Best Resource:** [Streamlit 30 Days Challenge](https://30days.streamlit.io/) (A fun, hands-on way to learn).

---

## 3. 🧠 AI & Machine Learning Concepts

### **RAG (Retrieval-Augmented Generation)**
The core architecture of this project. It means "looking up relevant info" (Retrieval) before "answering" (Generation).
- **Concept:** [What is RAG? (IBM)](https://www.ibm.com/topics/retrieval-augmented-generation)
- **Deep Dive:** [Pinecone Learning Center](https://www.pinecone.io/learn/retrieval-augmented-generation/)

### **Vector Embeddings**
How we turn text into numbers so the computer can understand "similarity".
- **Library Used:** `sentence-transformers` (specifically `all-MiniLM-L6-v2`).
- **Learn:** [Hugging Face Embeddings Course](https://huggingface.co/learn/nlp-course/chapter1/1)

### **Vector Database (ChromaDB)**
Where we store those embeddings to search them quickly.
- **Why we used it:** It's open-source and runs locally (no cloud account needed).
- **Docs:** [ChromaDB Verified Guide](https://docs.trychroma.com/getting-started)

### **LLM (Large Language Model)**
The "Brain" that answers the question. We used Google's Gemini.
- **Model Used:** `gemini-2.0-flash`.
- **docs:** [Google AI Studio Quickstart](https://ai.google.dev/tutorials/python_quickstart)

---

## 4. 🛠️ Utilities

### **PDF Parsing**
- **Library:** `pdfplumber`.
- **Task:** Extracting clean text from PDF files.
- **Docs:** [pdfplumber GitHub](https://github.com/jsvine/pdfplumber)

---

## 🚀 Recommended Learning Path for You

1.  **Master Python** basics if you haven't already.
2.  **Build a simple Hello World API** with FastAPI.
3.  **Build a simple Dashboard** with Streamlit.
4.  **HuggingFace Course**: Run through the "Embeddings" section to understand how text becomes numbers.
5.  **Build this project from scratch**: Try to re-write the `chunk_text` or `search_vector_store` functions yourself!
