# 📺 YouTube RAG Example

This subfolder demonstrates how to build a Retrieval-Augmented Generation workflow for YouTube videos. It ingests a transcript into Qdrant and then queries it using OpenAI embeddings.

## Files

- `yt_rag_ingestion.py` – downloads a video transcript, splits it into chunks and stores them in Qdrant
- `yt_rag_retrieval.py` – retrieves relevant chunks and queries GPT with timestamped context
- `data.txt` – raw transcript saved by the ingestion script

## Setup

1. Ensure Qdrant is running locally on `localhost:6333` (see the parent folder for `docker-compose.yml`).
2. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=your-key
   ```
3. Install dependencies from the repository root:
   ```bash
   pip install -r requirements.txt
   ```

## Running

```bash
python yt_rag_ingestion.py   # fetch transcript and store embeddings
python yt_rag_retrieval.py   # ask questions against the transcript
```
