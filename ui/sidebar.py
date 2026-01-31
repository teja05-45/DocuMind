import streamlit as st
from rag.kb_state import load_kb_state


def render_sidebar():
    with st.sidebar:
        st.markdown("## 🤖 DocuMind")
        st.caption("Source-grounded answers with citations 🔎")

        # -------------------------
        # ✅ GROQ SETTINGS CARD
        # -------------------------
        st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">⚡ Groq Settings</div>', unsafe_allow_html=True)

        groq_api_key = st.text_input(
            "🔑 Groq API Key",
            type="password",
            placeholder="Enter your Groq API Key here..."
        )

        groq_model = st.selectbox(
            "🧠 Select Groq Model",
            options=[
                "llama-3.1-8b-instant",
                "llama-3.1-70b-versatile",
                "mixtral-8x7b-32768",
                "gemma2-9b-it"
            ],
            index=0
        )

        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------------
        # ✅ CONTROLS CARD
        # -------------------------
        st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">⚡ Controls</div>', unsafe_allow_html=True)

        new_chat = st.button("➕ New Chat", use_container_width=True)
        clear_kb = st.button("🧹 Clear Knowledge Base", use_container_width=True)
        clear_chat = st.button("🗑 Clear Chat", use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------------
        # ✅ ADD SOURCES CARD
        # -------------------------
        st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">📂 Add Sources</div>', unsafe_allow_html=True)

        uploaded_files = st.file_uploader(
            "Upload PDF / DOCX / TXT",
            type=["pdf", "docx", "txt"],
            accept_multiple_files=True
        )

        url = st.text_input(
            "🔗 Website URL",
            placeholder="https://example.com"
        )

        notes = st.text_area(
            "📝 Paste Notes",
            height=110,
            placeholder="Paste any notes / text here..."
        )

        st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
        ingest = st.button("✅ Add to Knowledge Base", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        # -------------------------
        # ✅ INDEXED SOURCES CARD
        # -------------------------
        st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-title">📌 Indexed Sources</div>', unsafe_allow_html=True)

        kb_sources = load_kb_state()
        if not kb_sources:
            st.caption("No sources indexed yet.")
        else:
            unique = []
            seen = set()
            for s in kb_sources:
                name = s.get("source", "unknown")
                if name not in seen:
                    unique.append(s)
                    seen.add(name)

            for item in unique[:8]:
                st.write(f"✅ {item.get('source')}")

            if len(unique) > 8:
                st.caption(f"+ {len(unique) - 8} more sources")

        st.caption("✅ Answers only from sources (No hallucination)")
        st.markdown("</div>", unsafe_allow_html=True)

    return (
        uploaded_files,
        url,
        notes,
        ingest,
        clear_chat,
        new_chat,
        clear_kb,
        groq_api_key,
        groq_model
    )
