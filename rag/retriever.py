from __future__ import annotations
import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

VECTORSTORE_DIR = "data/vectorstore"


def get_embedding_model():
    """
    ✅ Must match the embedding model used in ingest.py
    """
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


def get_vectorstore():
    faiss_path = os.path.join(VECTORSTORE_DIR, "index.faiss")
    if not os.path.exists(faiss_path):
        return None

    embeddings = get_embedding_model()
    db = FAISS.load_local(VECTORSTORE_DIR, embeddings, allow_dangerous_deserialization=True)
    return db


def get_retriever(k: int = 4):
    db = get_vectorstore()
    if db is None:
        return None
    return db.as_retriever(search_kwargs={"k": k})
