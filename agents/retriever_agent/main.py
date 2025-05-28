from fastapi import FastAPI, Query
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.on_event("startup")
def load_docs():
    global vectorstore
    base_path = Path(__file__).parent
    file_path = base_path / "data" / "tech_earnings.txt"

    loader = TextLoader(str(file_path))
    docs = loader.load()

    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    split_docs = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(split_docs, embeddings)

@app.get("/")
def root():
    return {"message": "Retriever Agent is live. Use /search?q=your_question"}

@app.get("/search")
def search(q: str):
    try:
        results = vectorstore.similarity_search(q, k=2)
        return {"matches": [r.page_content for r in results]}
    except Exception as e:
        return {"error": str(e)}
