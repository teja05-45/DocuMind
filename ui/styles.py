import streamlit as st


def inject_global_css():
    st.markdown(
        """
        <style>
        /* =========================================================
           ✅ CORE: HIDE DEFAULT STREAMLIT UI
           ========================================================= */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* =========================================================
           ✅ APP THEME (GROQ STYLE)
           ========================================================= */
        .stApp {
            background: #0b1020;
            color: #e8e8e8;
        }

        section[data-testid="stSidebar"] {
            background: #0f172a;
            border-right: 1px solid rgba(255,255,255,0.06);
        }

        * {
            transition: all 0.18s ease-in-out;
        }

        /* =========================================================
           ✅ PLACEHOLDERS (VISIBLE)
           ========================================================= */
        input::placeholder, textarea::placeholder {
            color: rgba(255,255,255,0.88) !important;
            opacity: 1 !important;
        }

        /* =========================================================
           ✅ SIDEBAR CARDS + TITLES
           ========================================================= */
        .sidebar-card {
            background: rgba(255,255,255,0.035) !important;
            border: 1px solid rgba(244,114,182,0.22) !important;
            border-radius: 18px !important;
            padding: 12px !important;
            margin-bottom: 14px !important;
            box-shadow: 0 12px 34px rgba(0,0,0,0.28);
            backdrop-filter: blur(10px);
        }

        .sidebar-card:hover {
            border: 1px solid rgba(244,114,182,0.35) !important;
            box-shadow: 0 0 0 3px rgba(244,114,182,0.12), 0 16px 45px rgba(0,0,0,0.35);
            transform: translateY(-1px);
        }

        .sidebar-title {
            font-size: 13px !important;
            font-weight: 900 !important;
            margin-bottom: 8px !important;
            background: linear-gradient(
                90deg,
                rgba(244,114,182,1),
                rgba(216,180,254,1)
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Sidebar labels (keeps color theme) */
        section[data-testid="stSidebar"] label {
            color: rgba(244,114,182,0.92) !important;
            font-weight: 800 !important;
        }

        /* =========================================================
           ✅ SIDEBAR INPUTS
           ========================================================= */
        section[data-testid="stSidebar"] input,
        section[data-testid="stSidebar"] textarea {
            background: rgba(15,23,42,0.95) !important;
            color: #ffffff !important;
            border: 1px solid rgba(216,180,254,0.25) !important;
            border-radius: 14px !important;
        }

        /* ✅ Neon focus */
        section[data-testid="stSidebar"] input:focus,
        section[data-testid="stSidebar"] textarea:focus,
        div[data-testid="stChatInput"] textarea:focus {
            border: 1px solid rgba(244,114,182,0.85) !important;
            box-shadow: 0 0 0 4px rgba(244,114,182,0.20) !important;
        }

        /* =========================================================
           ✅ GROQ MODEL SELECTBOX (VISIBLE)
           ========================================================= */
        section[data-testid="stSidebar"] div[data-testid="stSelectbox"] div[role="combobox"] {
            background: rgba(15,23,42,0.98) !important;
            border: 2px solid rgba(216,180,254,0.45) !important;
            border-radius: 14px !important;
            padding: 4px 8px !important;
        }

        section[data-testid="stSidebar"] div[data-testid="stSelectbox"] div[role="combobox"] * {
            color: #ffffff !important;
            opacity: 1 !important;
            font-weight: 800 !important;
        }

        /* =========================================================
           ✅ FILE UPLOADER (FIX WHITE BOX + TEXT VISIBILITY)
           ========================================================= */

        /* Outer uploader box */
        section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
            background: rgba(15,23,42,0.96) !important;
            border: 1px solid rgba(244,114,182,0.35) !important;
            border-radius: 16px !important;
            padding: 12px !important;
        }

        /* Dropzone dark (removes the WHITE upload area) */
        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] {
            background: rgba(15,23,42,0.98) !important;
            border: 2px dashed rgba(244,114,182,0.75) !important;
            border-radius: 18px !important;
            padding: 16px !important;
        }

        /* Remove internal white container backgrounds */
        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] > div {
            background: transparent !important;
        }

        /* Text inside dropzone (Drag and drop + Limit...) */
        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] span,
        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] small,
        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] p {
            color: rgba(255,255,255,0.95) !important;
            opacity: 1 !important;
            visibility: visible !important;
            font-weight: 800 !important;
        }

        /* Browse files button */
        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] button {
            background: rgba(244,114,182,0.22) !important;
            border: 2px solid rgba(244,114,182,0.85) !important;
            color: #ffffff !important;
            font-weight: 900 !important;
            border-radius: 14px !important;
            padding: 10px 16px !important;
        }

        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] button * {
            color: #ffffff !important;
            opacity: 1 !important;
            visibility: visible !important;
        }

        section[data-testid="stSidebar"] div[data-testid="stFileUploaderDropzone"] button:hover {
            background: rgba(244,114,182,0.35) !important;
            box-shadow: 0 0 0 4px rgba(244,114,182,0.20) !important;
            transform: translateY(-1px);
        }

        /* =========================================================
           ✅ SIDEBAR BUTTONS
           ========================================================= */
        section[data-testid="stSidebar"] .stButton button {
            background: rgba(255,255,255,0.06) !important;
            border: 1px solid rgba(244,114,182,0.35) !important;
            color: #ffffff !important;
            padding: 10px 12px !important;
            border-radius: 14px !important;
            font-weight: 800 !important;
        }

        section[data-testid="stSidebar"] .stButton button:hover {
            background: rgba(255,255,255,0.09) !important;
            transform: translateY(-1px);
            box-shadow: 0 0 0 3px rgba(216,180,254,0.12),
                        0 0 18px rgba(244,114,182,0.12);
        }

        /* Welcome page (disabled buttons should still be visible) */
        .stButton button:disabled {
            opacity: 1 !important;
            color: rgba(255,255,255,0.98) !important;
            background: rgba(216,180,254,0.14) !important;
            border: 1px solid rgba(244,114,182,0.35) !important;
        }

        /* =========================================================
           ✅ TOPBAR (HEADER)
           ========================================================= */
        .topbar {
            max-width: 980px;
            margin: auto;
            padding: 10px 6px 14px 6px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }

        .topbar-left {
            display: flex;
            flex-direction: column;
            gap: 2px;
        }

        .app-title {
            font-size: 18px;
            font-weight: 900;
            background: linear-gradient(
                90deg,
                rgba(244,114,182,1),
                rgba(216,180,254,1)
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .app-subtitle {
            font-size: 12px;
            opacity: 0.9;
            color: rgba(216,180,254,0.88);
        }

        .status-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 10px;
            border-radius: 999px;
            border: 1px solid rgba(255,255,255,0.12) !important;
            background: linear-gradient(
                90deg,
                rgba(244,114,182,0.20),
                rgba(216,180,254,0.20)
            ) !important;
            font-size: 12px;
            opacity: 0.95;
        }

        .dot {
            width: 8px;
            height: 8px;
            border-radius: 999px;
            background: #22c55e;
            display: inline-block;
        }

        /* =========================================================
           ✅ CHAT UI
           ========================================================= */
        .chat-wrapper {
            max-width: 980px;
            margin: auto;
            padding: 0.6rem 0.3rem 1rem 0.3rem;
        }

        .bubble-row {
            width: 100%;
            display: flex;
            margin: 10px 0px;
        }
        .assistant-row { justify-content: flex-start; }
        .user-row { justify-content: flex-end; }

        .bubble {
            max-width: 78%;
            padding: 12px 14px;
            border-radius: 16px;
            line-height: 1.6;
            font-size: 15px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.15);
            word-wrap: break-word;
            animation: fadeInUp 0.22s ease-in-out;
        }

        .user-bubble {
            background: rgba(244,114,182,0.16);
            border: 1px solid rgba(244,114,182,0.45);
        }

        .assistant-bubble {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.08);
        }

        .role-label {
            font-size: 12px;
            opacity: 0.85;
            margin-bottom: 6px;
            color: rgba(216,180,254,0.90);
        }

        /* ✅ Dark chat input */
        div[data-testid="stChatInput"] textarea {
            background: rgba(15,23,42,0.96) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255,255,255,0.14) !important;
            border-radius: 16px !important;
        }

        @keyframes fadeInUp {
            from { transform: translateY(6px); opacity: 0.0; }
            to { transform: translateY(0px); opacity: 1.0; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
