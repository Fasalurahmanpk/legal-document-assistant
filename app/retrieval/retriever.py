import chromadb

from app.embeddings.embedder import generate_embedding

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="legal_docs"
)


def retrieve(query, n_results=2):

    query_embedding = generate_embedding(query)

    results = collection.query(
    query_embeddings=[
        query_embedding.tolist()
    ],
    n_results=3,
    include=[
        "documents",
        "metadatas"
    ]
    )

    return results



