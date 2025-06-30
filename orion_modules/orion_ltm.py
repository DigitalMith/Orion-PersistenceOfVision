import os
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

os.environ["CHROMA_TELEMETRY_ENABLED"] = "FALSE"

client = chromadb.PersistentClient(path="./memory/chroma_db/")
embedder = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

collection = client.get_or_create_collection(
    name="orion_memory",
    embedding_function=embedder
)

def add_memory(content: str, metadata: dict = None, uid: str = None):
    from uuid import uuid4
    uid = uid or str(uuid4())
    collection.add(
        documents=[content],
        ids=[uid],
        metadatas=[metadata or {}]
    )
    return uid

def query_memory(prompt: str, n=3):
    return collection.query(query_texts=[prompt], n_results=n)
