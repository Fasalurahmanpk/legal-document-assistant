import os
import tempfile

from app.ingestion.pdf_loader import load_pdf
from app.ingestion.chunker import chunk_text
from app.embeddings.embedder import generate_embedding
from app.retrieval.retriever import collection


def process_uploaded_pdf(uploaded_file):

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:

        temp_file.write(uploaded_file.getbuffer())

        temp_path = temp_file.name

    # Extract text
    text = load_pdf(temp_path)

    # Delete temporary file
    os.remove(temp_path)

    # Chunk text
    chunks = chunk_text(text)

    # Store in ChromaDB
    for i, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        collection.add(
            ids=[f"{uploaded_file.name}_{i}"],
            documents=[chunk],
            embeddings=[embedding.tolist()],
            metadatas=[

                {
                    "source": uploaded_file.name,
                    "chunk": i
                }

            ]
        )

    return len(chunks)