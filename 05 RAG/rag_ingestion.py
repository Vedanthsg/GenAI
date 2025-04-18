from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_qdrant import QdrantVectorStore

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
pdf_path = "Data\\the-white-tiger.pdf"
loader = PyPDFLoader(file_path = pdf_path)
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
    collection_name="learning_langchain",
    embedding=embeddings,
)

vector_store.add_documents(documents=split_docs)
