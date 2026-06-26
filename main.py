from app.ingestion.document_loader import load_documents
from app.ingestion.chunker import chunk_text
from app.embeddings.embedder import generate_embedding

import chromadb

documents = load_documents(
    "data/documents"
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

try:
    client.delete_collection("legal_docs")
except:
    pass

collection = client.get_or_create_collection(
    name="legal_docs"
)

chunk_counter = 0

for doc in documents:

    source = doc["source"]

    chunks = chunk_text(
        doc["text"]
    )

    for chunk in chunks:

        embedding = generate_embedding(
            chunk
        )

        collection.add(
            ids=[str(chunk_counter)],
            documents=[chunk],
            embeddings=[
                embedding.tolist()
            ],
            metadatas=[
                {
                    "source": source,
                    "chunk_id": chunk_counter
                }
            ]
        )

        chunk_counter += 1

print(
    f"Stored {chunk_counter} chunks"
)


documents = load_documents(
    "data/documents"
)

for doc in documents:

    source = doc["source"]

    chunks = chunk_text(
        doc["text"]
    )

    # ADD THESE LINES HERE
    print(f"\nDocument: {source}")
    print(f"Characters: {len(doc['text'])}")
    print(f"Chunks: {len(chunks)}")

    for chunk in chunks:

        embedding = generate_embedding(
            chunk
        )

        collection.add(
            ids=[str(chunk_counter)],
            documents=[chunk],
            embeddings=[embedding.tolist()],
            metadatas=[
                {
                    "source": source,
                    "chunk_id": chunk_counter
                }
            ]
        )

        chunk_counter += 1