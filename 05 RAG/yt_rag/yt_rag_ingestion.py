from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_qdrant import QdrantVectorStore
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

load_dotenv()

url = "https://www.youtube.com/watch?v=yviJikU4gwk"

def extract_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)

    if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            query = parse_qs(parsed_url.query)
            return query.get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/embed/')[1]
        elif parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/v/')[1]
    elif parsed_url.hostname == 'youtu.be':
        return parsed_url.path.lstrip('/')
    return None

video_id = extract_video_id(url)

ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id)
raw_data = fetched_transcript.to_raw_data()

with open("data.txt", "w", encoding="utf-8") as file:
    file.write(str(raw_data))
print("Transcript saved to transcript.txt")

api_key = os.getenv("OPENAI_API_KEY")
file_path = "data.txt"
loader = TextLoader(file_path = file_path)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)

split_docs = text_splitter.split_documents(documents=docs)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=api_key
)

vector_store = QdrantVectorStore.from_documents(
    documents=[],
    url="http://localhost:6333",
    collection_name="yt-rag",
    embedding=embeddings,
)

vector_store.add_documents(documents=split_docs)
print("Ingestion Done!")