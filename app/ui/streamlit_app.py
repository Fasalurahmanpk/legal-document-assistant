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
from app.utils.upload_processor import process_uploaded_pdf


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Legal RAG Assistant",
    page_icon="⚖️",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("⚖️ Legal RAG Assistant")

st.markdown(
    """
Upload legal PDF documents, process them into a vector database,
and ask questions using Retrieval-Augmented Generation (RAG).
"""
)

st.divider()

# ======================================================
# Upload Section
# ======================================================

st.subheader("📄 Upload Legal Documents")

uploaded_files = st.file_uploader(
    "Choose one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.write("### Selected Files")

    for file in uploaded_files:

        st.write(f"📄 {file.name}")

    if st.button("📥 Process Documents"):

        total_chunks = 0

        with st.spinner("🔄 Processing uploaded documents..."):

            for uploaded_file in uploaded_files:

                chunks = process_uploaded_pdf(
                    uploaded_file
                )

                total_chunks += chunks

        st.success(
            f"✅ Successfully processed {len(uploaded_files)} document(s)"
        )

        st.info(
            f"📚 Total Chunks Stored : {total_chunks}"
        )

st.divider()

# ======================================================
# Question Section
# ======================================================

st.subheader("❓ Ask a Question")

query = st.text_input(
    "Enter your question",
    placeholder="Example: What is the license grant?"
)

if st.button("🚀 Get Answer"):

    if not query.strip():

        st.warning("Please enter a question.")

    else:

        # Retrieve Context
        with st.spinner("🔍 Retrieving relevant legal clauses..."):

            results = retrieve(query)

            context = "\n".join(
                results["documents"][0]
            )

        # Generate Answer
        with st.spinner("🤖 Generating answer..."):

            answer = generate_answer(
                query,
                context
            )

        st.divider()

        # -----------------------------
        # Answer
        # -----------------------------
        st.subheader("📄 Answer")

        st.markdown(answer)

        st.divider()

        # -----------------------------
        # Sources
        # -----------------------------
        st.subheader("📚 Sources")

        seen = set()

        for metadata in results["metadatas"][0]:

            source = metadata["source"]

            if source not in seen:

                st.success(source)

                seen.add(source)

        # -----------------------------
        # Retrieved Context
        # -----------------------------
        with st.expander("🔍 View Retrieved Context"):

            st.write(context)