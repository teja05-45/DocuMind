# 🧠 DocuMind — Groq RAG Assistant (ChatGPT-style UI)

A modern ChatGPT/Gemini-style **RAG (Retrieval-Augmented Generation)** chatbot that answers questions strictly from **your uploaded PDFs, DOCX, TXT files, website URLs, and notes** using **Groq + LangChain + FAISS** with **citations** and **anti-hallucination** rules.

✅ Fast • ✅ Source-grounded • ✅ Multi-file • ✅ Clean UI • ✅ Deployable

---

## 🚀 Features

### ✅ Supported Inputs
- 📄 Upload multiple **PDF**
- 📝 Upload **DOCX**
- 📃 Upload **TXT**
- 🔗 Add **Website URLs**
- ✍️ Paste Notes / Raw Text

### ✅ RAG Pipeline (No Hallucination)
- Extract + clean content
- Chunking & splitting
- Embeddings using `sentence-transformers`
- Vector storage using **FAISS**
- Top-k retrieval
- Groq LLM generation using retrieved context only
- ✅ If answer is not in the sources → refusal response

### ✅ UI (ChatGPT/Gemini Style)
- Modern dark theme (Groq-inspired)
- Sidebar knowledge panel
- Main chat area with chat bubbles
- Typing indicator + smooth animations
- Expandable sources section
- Auto-scroll to newest message

---

## 🏗️ System Architecture

### ✅ High-Level Flow

```
User Uploads / URL / Notes
        │
        ▼
Document Loaders (PDF/DOCX/TXT/URL/Text)
        │
        ▼
Text Cleaning + Normalization
        │
        ▼
Chunking (Recursive Splitter)
        │
        ▼
Embeddings (SentenceTransformers)
        │
        ▼
FAISS Vector Database (Local)
        │
        ▼
Retriever (Top-k Similarity Search)
        │
        ▼
Groq LLM (Answer from Context Only)
        │
        ▼
Final Answer + Citations (Sources)

```
```
DocuMind/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── rag/
│   ├── loaders.py          # Load PDF/DOCX/TXT/URLs/Notes into Documents
│   ├── ingest.py           # Chunking + Embeddings + Build/Update FAISS index
│   ├── retriever.py        # Load FAISS + return retriever
│   ├── chain.py            # Strict anti-hallucination Groq response pipeline
│   ├── kb_state.py         # Store KB source info (optional)
│
├── ui/
│   ├── styles.py           # Groq dark UI theme + CSS styling
│   ├── sidebar.py          # Sidebar (file upload, url, notes, model)
│   ├── chat.py             # Chat render UI (bubbles, sources, scroll, typing)
│
└── data/
    ├── uploads/            # Uploaded files (not committed)
    └── vectorstore/        # FAISS index (not committed)
```

🔒 Anti-Hallucination Strategy

DocuMind enforces context-only answering:

✅ Uses a strict system prompt:

Answer ONLY from retrieved context

If not present → respond with:

“I don’t have enough information from the provided sources to answer that.”

✅ Always returns citations:

Shows document filenames / URL references

Helps user verify source evidence

⚙️ Tech Stack
Component	Tool
UI	Streamlit
RAG Orchestration	LangChain
Vector DB	FAISS
Embeddings	SentenceTransformers (all-MiniLM-L6-v2)
LLM	Groq API (user key input via sidebar)
Data Sources	PDF, DOCX, TXT, URL scraping, notes
✅ Installation (Local Setup)
1️⃣ Clone Repository
```
git clone https://github.com/<your-username>/DocuMind.git
cd DocuMind
```


2️⃣ Create Virtual Environment
```
python -m venv .venv
```

Activate (Windows):
```
.venv\Scripts\activate\
```


3️⃣ Install Dependencies

```
pip install -r requirements.txt
```
4️⃣ Run App

```
streamlit run app.py
```

🔑 Groq API Key Setup

DocuMind does not store your API key.
You paste the key into the sidebar at runtime.

✅ Supported Groq models depend on your account access.

🧪 Testing Checklist

✅ Upload a PDF → Ask question from PDF → Answer should be correct
✅ Upload DOCX/TXT → Ask question → Answer uses file content
✅ Add URL → Ask question → Answer should use URL context
✅ Ask unrelated question → Should refuse safely ✅

☁️ Deployment Options

✅ Streamlit Cloud (recommended)
✅ Hugging Face Spaces
✅ Render
✅ Docker + VPS

Since Groq key is user-provided, deployment is secure and easy.

🛠️ Future Improvements

Multi-session chat history

Per-user knowledge base

Advanced citation preview (chunk-level highlight)

Hybrid search (BM25 + Vector)

LangGraph agent workflows

👨‍💻 Author

Built by Teja Matta

Project: DocuMind — AI Document Chat Assistant


