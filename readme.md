# ⚖️ Legal RAG Assistant

## Overview

Legal RAG Assistant is a Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions about legal documents and receive accurate, source-grounded answers. The system performs semantic search over multiple legal PDFs using vector embeddings and generates responses with a Large Language Model (Llama 3).

---

## Features

* Multi-document PDF ingestion
* Automatic text extraction from legal documents
* Semantic text chunking with overlap
* BGE (BAAI) embedding model for vector representation
* ChromaDB vector database for semantic retrieval
* Llama 3 via Groq API for answer generation
* Source document citations
* Streamlit web interface
* Fast semantic search across multiple legal agreements

---

## Tech Stack

* Python
* Streamlit
* ChromaDB
* Sentence Transformers (BAAI/BGE)
* Groq API
* Llama 3
* PyMuPDF (fitz)
* NumPy

---

## Project Structure

```text
legal_rag/
│
├── app/
│   ├── embeddings/
│   ├── generation/
│   ├── ingestion/
│   ├── retrieval/
│   └── ui/
│
├── chroma_db/
├── data/
│   └── documents/
│
├── main.py
├── test_model.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/legal-rag-assistant.git
cd legal-rag-assistant
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

### Build the Vector Database

Place your legal PDF documents inside:

```text
data/documents/
```

Then run:

```bash
python main.py
```

### Launch the Application

```bash
streamlit run app/ui/streamlit_app.py
```

---

## How It Works

1. Load legal PDF documents.
2. Extract text using PyMuPDF.
3. Split documents into overlapping chunks.
4. Generate semantic embeddings using BGE.
5. Store embeddings in ChromaDB.
6. Retrieve the most relevant chunks based on the user's question.
7. Generate a grounded response using Llama 3 through the Groq API.
8. Display the answer along with the source documents.

---

## Screenshots

Add screenshots here after deployment.

Example:

```
screenshots/
├── home.png
├── answer.png
├── retrieval.png
```

---

## Future Improvements

* PDF upload from the web interface
* Chat history
* Page-level citations
* Hybrid Search (BM25 + Vector Search)
* Metadata filtering
* RAG evaluation using RAGAS
* Docker support
* Authentication

---

## Author

**Fasalu Rahman P K**

M.Sc. Computer Science (Artificial Intelligence & Machine Learning)

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile
