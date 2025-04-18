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
    collection_name="yt-rag",
    embedding=embeddings,
)

relevant_chunks = retrieval.similarity_search(
    query="what is useRef hook"
)


SYSTEM_PROMPT = f"""
You are a helpful AI assistant who responds bassed on the available context. 
context:
{relevant_chunks} .
This Context contains transcript of a youtube video with timestamps. Now I want you to answer the question along with the starting and ending timestamps.

use the following example for the output
Example:
Query:  What is a Mobile Phone?
Response: A mobile phone or cell phone is a portable telephone that allows users to make and receive calls over a radio frequency link while moving within a designated telephone service area, unlike fixed-location phones.
"""

result = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        { "role": "user", "content": SYSTEM_PROMPT },
    ]
)

print(result.choices[0].message.content)