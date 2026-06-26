import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../.."
        )
    )
)

import streamlit as st

from app.retrieval.retriever import retrieve
from app.generation.generator import generate_answer

# Page Configuration
st.set_page_config(
    page_title="Legal RAG Assistant",
    page_icon="⚖️",
    layout="wide"
)

# Title
st.title("⚖️ Legal RAG Assistant")
st.markdown(
    "Ask questions about your legal documents and receive source-grounded answers."
)

# User Input
query = st.text_input(
    "Ask a question",
    placeholder="e.g. What is the license grant?"
)

# Submit Button
if st.button("Submit"):

    if not query.strip():

        st.warning("Please enter a question.")

    else:

        # Retrieval Spinner
        with st.spinner("🔍 Retrieving relevant legal clauses..."):

            results = retrieve(query)

            context = "\n".join(
                results["documents"][0]
            )

        # Generation Spinner
        with st.spinner("🤖 Generating answer..."):

            answer = generate_answer(
                query,
                context
            )

        # Display Answer
        st.subheader("📄 Answer")
        st.markdown(answer)

        # Display Sources
        st.subheader("📚 Sources")

        seen = set()

        for metadata in results["metadatas"][0]:

            source = metadata["source"]

            if source not in seen:

                st.success(source)

                seen.add(source)