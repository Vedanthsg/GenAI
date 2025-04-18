# 🧠 Retrieval-Augmented Generation (RAG) with LangChain, Qdrant, and OpenAI

This project demonstrates how to build a local RAG pipeline using LangChain, Qdrant, and OpenAI embeddings. It supports document ingestion and intelligent retrieval for both **PDF files** and **YouTube video transcripts**.

---

## 📦 Features

- ✅ Ingest PDF documents using `PyPDFLoader`
- ✅ Ingest YouTube transcripts using `YouTubeTranscriptApi`
- ✅ Embed text with OpenAI's `text-embedding-3-large`
- ✅ Store and query embeddings using `QdrantVectorStore`
- ✅ Local Qdrant setup via `docker-compose`
- ✅ Retrieve relevant information based on user queries
- ✅ Generate responses using OpenAI GPT (with optional timestamped context for YouTube)

---

## 🗂️ Project Structure

```
.
├── docker-compose.yml           # Qdrant vector DB service
├── rag_ingestion.py             # PDF ingestion and embedding
├── rag_retrieval.py             # PDF-based RAG querying
├── yt_rag_ingestion.py          # YouTube transcript ingestion and embedding
├── yt_rag_retrieval.py          # YouTube-based RAG querying with timestamps
├── data.txt                     # Raw YouTube transcript
└── .env                         # OpenAI API key (not included)
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag-langchain-qdrant.git
cd rag-langchain-qdrant
```

### 2. Setup Environment

Create a `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

### 3. Start Qdrant Vector Store

```bash
docker-compose up -d
```

---

## 🧾 PDF Workflow

### 🔍 Ingestion

```bash
python rag_ingestion.py
```

### 🤖 Retrieval

```bash
python rag_retrieval.py
```

---

## 📺 YouTube Workflow

### 🔍 Ingestion

```bash
python yt_rag_ingestion.py
```

This script:
- Extracts video ID from a YouTube URL
- Fetches transcript
- Saves transcript to `data.txt`
- Embeds and stores in Qdrant

### 🤖 Retrieval (with timestamps)

```bash
python yt_rag_retrieval.py
```

---

## 📌 Example Use Cases

- 📝 Summarizing long documents
- 📽️ Explaining YouTube video content
- 🤖 Chatbot with domain-specific context

---

## 📚 Dependencies

Install via:

```bash
pip install -r requirements.txt
```

You may need:

- `langchain`
- `qdrant-client`
- `openai`
- `python-dotenv`
- `youtube-transcript-api`

---

## 🛠️ Notes

- Ensure Qdrant is running locally at `localhost:6333`.
- The YouTube ingestion script saves transcript to `data.txt`, which is then used for embedding.

