# 🧠 Decoding AI Jargons

Welcome to **Decoding AI Jargons** — a simplified guide and accompanying codebase to help you understand the complex terms behind AI and Large Language Models (LLMs), especially for beginners and enthusiasts.

🔗 **Read the full blog here**: [https://vedanth-genai.hashnode.dev/decoding-ai-jargons](https://vedanth-genai.hashnode.dev/decoding-ai-jargons)

---

## 📘 Overview

AI terminology can often feel overwhelming — from transformers and tokenization to embeddings and self-attention. This repository contains:
- A detailed article explaining core AI concepts in a simple and relatable way.
- Example code that demonstrates how tokenization and embeddings work using OpenAI APIs and `tiktoken`.

---

## 📝 Article Summary

**Topics Covered**:
- Transformers, Encoder, Decoder
- Vectors, Embeddings, Positional Encoding
- Semantic Meaning, Self-Attention, Softmax
- Multi-Head Attention, Temperature, Knowledge Cutoff
- Tokenization, Vocab Size

👉 Check out the article here: [Decoding AI Jargons Blog](https://vedanth-genai.hashnode.dev/decoding-ai-jargons)

---

## 🧪 Code Samples

### 1. `tokenization.py`

A simple script using `tiktoken` to:
- Tokenize text into integers
- Decode tokens back to readable text
- Display vocabulary size

📂 **Run it using**:
```bash
python tokenization.py
```

---

### 2. `embeddings.py`

Demonstrates how to use OpenAI’s API to:
- Convert input text into high-dimensional vector embeddings

⚠️ Requires `.env` file with your OpenAI API key:
```bash
OPENAI_API_KEY=your_key_here
```

📂 **Run it using**:
```bash
python embeddings.py
```

---

## 💡 Prerequisites

- Python 3.8+
- Install dependencies:
```bash
pip install openai python-dotenv tiktoken
```

---

## 📂 Files Included

| File             | Description                                 |
|------------------|---------------------------------------------|
| `ARTICLE.md`     | Blog-style markdown content for easy reuse |
| `tokenization.py`| Code to demonstrate tokenization           |
| `embeddings.py`  | Code to generate vector embeddings          |


