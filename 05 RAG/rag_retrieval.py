from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

client = OpenAI()

api_key = os.getenv("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=api_key
)

retrieval = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_langchain",
    embedding=embeddings,
)

relevant_chunks = retrieval.similarity_search(
    query="who is the main character"
)


SYSTEM_PROMPT = f"""
You are a helpful AI assistant who responds bassed on the available context. 
context:
{relevant_chunks} 
"""

result = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        { "role": "user", "content": SYSTEM_PROMPT },
    ]
)

print(result.choices[0].message.content)