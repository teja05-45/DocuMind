from __future__ import annotations
from typing import List, Dict, Any

from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from rag.prompts import STRICT_RAG_PROMPT


def format_context(docs: List[Document]) -> str:
    formatted = []
    for i, d in enumerate(docs, start=1):
        src = d.metadata.get("source", "unknown")
        p = d.metadata.get("page", None)
        page_info = f" (page {p})" if p is not None else ""
        formatted.append(f"[{i}] SOURCE: {src}{page_info}\nCONTENT: {d.page_content}")
    return "\n\n".join(formatted)


def build_llm(groq_api_key: str, model_name: str):
    return ChatGroq(
        model=model_name,
        temperature=0,
        groq_api_key=groq_api_key
    )


def generate_answer(
    question: str,
    retrieved_docs: List[Document],
    groq_api_key: str,
    model_name: str
) -> Dict[str, Any]:

    # ✅ strict refusal
    if not retrieved_docs:
        return {
            "answer": "I don’t have enough information from the provided sources to answer that.",
            "sources": []
        }

    context = format_context(retrieved_docs)

    prompt = PromptTemplate(
        template=STRICT_RAG_PROMPT,
        input_variables=["context", "question"],
    )

    llm = build_llm(groq_api_key=groq_api_key, model_name=model_name)

    final_prompt = prompt.format(context=context, question=question)
    response = llm.invoke(final_prompt)

    # ✅ citations
    sources = []
    for d in retrieved_docs:
        src = d.metadata.get("source", "unknown")
        page = d.metadata.get("page", None)
        if page is not None:
            sources.append(f"{src} (page {page})")
        else:
            sources.append(str(src))

    # unique sources
    seen = set()
    unique_sources = []
    for s in sources:
        if s not in seen:
            unique_sources.append(s)
            seen.add(s)

    return {
        "answer": response.content.strip(),
        "sources": unique_sources
    }
