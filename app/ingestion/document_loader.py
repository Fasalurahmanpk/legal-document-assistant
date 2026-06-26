import os

from app.ingestion.pdf_loader import load_pdf
from app.ingestion.text_loader import load_text


def load_documents(folder):

    documents = []

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        if file.endswith(".pdf"):
            text = load_pdf(path)
        elif file.endswith(".txt"):
            text = load_text(path)
        else:
            continue

        documents.append(
            {
                "source": file,
                "text": text,
            }
        )

    return documents
