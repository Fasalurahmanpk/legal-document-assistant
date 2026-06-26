from app.retrieval.retriever import retrieve
from app.generation.generator import generate_answer

query = "What are the conditions of employment?"

results = retrieve(query)

context = "\n".join(
    results["documents"][0]
)

answer = generate_answer(
    query,
    context
)

print("\nQUESTION:")
print(query)

print("\nANSWER:")
print(answer)

print("\nSOURCES:")


seen = set()

for metadata in results["metadatas"][0]:

    source = metadata["source"]

    if source not in seen:

        print(source)

        seen.add(source)