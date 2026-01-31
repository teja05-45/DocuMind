from __future__ import annotations
from typing import List
import os
import shutil

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from rag.kb_state import save_kb_state


VECTORSTORE_DIR = "data/vectorstore"


def get_text_splitter():
    return RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " ", ""],
    )


def get_embedding_model():
    """
    ✅ Fully local embeddings (NO Ollama dependency)
    Fast + small + works great for RAG
    """
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def build_or_update_faiss(docs: List[Document]) -> FAISS:
    os.makedirs(VECTORSTORE_DIR, exist_ok=True)

    splitter = get_text_splitter()
    chunks = splitter.split_documents(docs)

    embeddings = get_embedding_model()

    if os.path.exists(os.path.join(VECTORSTORE_DIR, "index.faiss")):
        db = FAISS.load_local(VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)
        db.add_documents(chunks)
    else:
        db = FAISS.from_documents(chunks, embeddings)

    # ✅ Save indexed sources (for sidebar display)
    source_list = []
    for d in chunks:
        source_list.append({
            "source": d.metadata.get("source", "unknown"),
            "type": d.metadata.get("type", "unknown"),
            "page": d.metadata.get("page", None),
        })

    save_kb_state(source_list)

    db.save_local(VECTORSTORE_DIR)
    return db


def clear_vectorstore():
    if os.path.exists(VECTORSTORE_DIR):
        shutil.rmtree(VECTORSTORE_DIR)
    os.makedirs(VECTORSTORE_DIR, exist_ok=True)
