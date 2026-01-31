import os
import streamlit as st

from ui.styles import inject_global_css
from ui.sidebar import render_sidebar
from ui.chat import init_chat_state, render_topbar, render_messages, chat_input_box

from rag.loaders import load_pdf, load_docx, load_txt, load_url, load_notes
from rag.ingest import build_or_update_faiss, clear_vectorstore
from rag.retriever import get_retriever
from rag.chain import generate_answer


# ---------------------------
# Config
# ---------------------------
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ---------------------------
# Streamlit Setup
# ---------------------------
st.set_page_config(page_title="DocuMind", page_icon="🤖", layout="wide")
inject_global_css()
init_chat_state()


# ---------------------------
# Sidebar
# ---------------------------
(
    uploaded_files,
    url,
    notes,
    ingest,
    clear_chat,
    new_chat,
    clear_kb,
    groq_api_key,
    groq_model
) = render_sidebar()


# ---------------------------
# Sidebar Actions
# ---------------------------
if new_chat:
    st.session_state.messages = []
    st.session_state.is_typing = False
    st.rerun()

if clear_chat:
    st.session_state.messages = []
    st.session_state.is_typing = False
    st.rerun()

if clear_kb:
    clear_vectorstore()
    st.success("✅ Knowledge Base cleared successfully!")
    st.rerun()


# ---------------------------
# Helpers
# ---------------------------
def save_uploaded_file(uploaded_file):
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path


def groq_key_valid(key: str) -> bool:
    return bool(key and key.strip() and len(key.strip()) > 20)


# ---------------------------
# KB Ready Status + Topbar
# ---------------------------
retriever = get_retriever(k=4)
kb_ready = retriever is not None

render_topbar(model_name=f"Groq • {groq_model}", kb_ready=kb_ready)


# ---------------------------
# Ingestion
# ---------------------------
if ingest:
    with st.spinner("🔄 Indexing knowledge base... Please wait"):
        all_docs = []

        # ✅ Files
        if uploaded_files:
            for uf in uploaded_files:
                path = save_uploaded_file(uf)

                if uf.name.lower().endswith(".pdf"):
                    all_docs.extend(load_pdf(path))
                elif uf.name.lower().endswith(".docx"):
                    all_docs.extend(load_docx(path))
                elif uf.name.lower().endswith(".txt"):
                    all_docs.extend(load_txt(path))

        # ✅ URL
        if url and url.strip():
            try:
                all_docs.extend(load_url(url.strip()))
            except Exception as e:
                st.error(f"❌ URL load failed: {e}")

        # ✅ Notes
        if notes and notes.strip():
            all_docs.extend(load_notes(notes.strip(), title="User Notes"))

        if not all_docs:
            st.warning("⚠️ No data provided. Upload files / add URL / paste notes.")
        else:
            build_or_update_faiss(all_docs)
            st.success("✅ Knowledge Base updated successfully!")

    st.rerun()


# ---------------------------
# Chat UI
# ---------------------------
render_messages()
query = chat_input_box()

# ✅ FIX: ensure query is always string
if query is not None:
    query = str(query).strip()


# ---------------------------
# User Sends Query
# ---------------------------
if query:
    # ✅ Store user message
    st.session_state.messages.append({"role": "user", "content": query})

    # ✅ Validate Groq key
    if not groq_key_valid(groq_api_key):
        st.session_state.messages.append({
            "role": "assistant",
            "content": "⚠️ Please enter your **Groq API Key** in the sidebar to start chatting.",
            "sources": []
        })
        st.rerun()

    # ✅ Check KB exists
    retriever = get_retriever(k=4)
    if retriever is None:
        st.session_state.messages.append({
            "role": "assistant",
            "content": "⚠️ Knowledge base is empty. Upload files / add URL / paste notes first.",
            "sources": []
        })
        st.rerun()

    # ✅ Turn typing ON and rerun
    st.session_state.is_typing = True
    st.rerun()


# ---------------------------
# Generate Assistant Answer (after rerun)
# ---------------------------
if st.session_state.messages:
    last_msg = st.session_state.messages[-1]

    # ✅ If last message is user & typing is ON → generate assistant response
    if last_msg.get("role") == "user" and st.session_state.is_typing:
        user_query = str(last_msg.get("content", "")).strip()

        retriever = get_retriever(k=4)

        with st.spinner("🤖 Thinking..."):
            # ✅ NEW LangChain method
            retrieved_docs = retriever.invoke(user_query)

            result = generate_answer(
                question=user_query,
                retrieved_docs=retrieved_docs,
                groq_api_key=groq_api_key,
                model_name=groq_model
            )

        # ✅ Store assistant message
        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"],
            "sources": result["sources"]
        })

        # ✅ Turn typing OFF
        st.session_state.is_typing = False
        st.rerun()
