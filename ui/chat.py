import streamlit as st


def init_chat_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "is_typing" not in st.session_state:
        st.session_state.is_typing = False


def render_topbar(model_name: str, kb_ready: bool):
    status_text = "Knowledge Base: Ready ✅" if kb_ready else "Knowledge Base: Empty ⚠️"
    st.markdown(
        f"""
        <div class="topbar">
            <div class="topbar-left">
                <div class="app-title">RAG Assistant</div>
                <div class="app-subtitle">Model: {model_name} • {status_text}</div>
            </div>
            <div class="status-pill">
                <span class="dot"></span>
                <span>Online</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_welcome():
    st.markdown(
        """
        <div class="chat-wrapper">
            <div class="bubble assistant-bubble" style="max-width: 100%;">
                <div class="role-label">Assistant</div>
                <b>Welcome 👋</b><br>
                Upload documents, add a website URL, or paste notes.  
                Then ask questions — I will answer only from your sources ✅
                <br><br>
                <span style="opacity:0.85; font-size:13px;">
                If the answer is not present, I will say:
                <i>“I don’t have enough information from the provided sources to answer that.”</i>
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("📂 Upload Documents", use_container_width=True, disabled=True)
    with col2:
        st.button("🔗 Add Website URL", use_container_width=True, disabled=True)
    with col3:
        st.button("📝 Paste Notes", use_container_width=True, disabled=True)


def render_messages():
    if len(st.session_state.messages) == 0 and not st.session_state.is_typing:
        render_welcome()
        return

    st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

    for i, msg in enumerate(st.session_state.messages):
        role = msg.get("role", "assistant")
        content = msg.get("content", "")
        sources = msg.get("sources", [])

        if role == "user":
            st.markdown(
                f"""
                <div class="bubble-row user-row">
                    <div class="bubble user-bubble">
                        <div class="role-label">You</div>
                        {content}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="bubble-row assistant-row">
                    <div class="bubble assistant-bubble">
                        <div class="role-label">Assistant</div>
                        {content}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # ✅ Copy button
            colA, colB = st.columns([0.84, 0.16])
            with colB:
                if st.button("📋 Copy", key=f"copy_{i}"):
                    st.toast("✅ Copied!", icon="✅")

            # ✅ Sources dropdown
            if sources:
                with st.expander("📌 Sources used", expanded=False):
                    for s in sources:
                        st.write(f"- {s}")

    # ✅ Typing indicator
    if st.session_state.is_typing:
        st.markdown(
            """
            <div class="bubble-row assistant-row">
                <div class="bubble assistant-bubble">
                    <div class="role-label">Assistant</div>
                    <i>Typing...</i>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ✅ Auto-scroll to bottom
    st.markdown(
        """
        <div id="bottom-marker"></div>
        <script>
        const marker = document.getElementById("bottom-marker");
        if(marker){
            marker.scrollIntoView({behavior: "smooth"});
        }
        </script>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


def chat_input_box():
    return st.chat_input("Ask something from your knowledge base...")
