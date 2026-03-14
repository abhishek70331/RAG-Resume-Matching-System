import chromadb
import uuid
import os

from utils import load_resumes
from chunker import chunk_documents
from embeddings import generate_embedding
from metadata_extractor import extract_metadata


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RESUME_FOLDER = os.path.join(BASE_DIR, "data", "resumes")

client = chromadb.PersistentClient(path="../chroma_db")

collection = client.get_or_create_collection(name="resumes")


def build_rag():

    print("Loading resumes...")

    documents = load_resumes(RESUME_FOLDER)

    print("Chunking documents...")

    chunks = chunk_documents(documents)

    print("Generating embeddings and storing...")

    for chunk in chunks:

        text = chunk.page_content

        embedding = generate_embedding(text)

        metadata = extract_metadata(text)

        metadata["resume_path"] = chunk.metadata["source"]

        collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[str(uuid.uuid4())]
        )

    print("Vector DB created successfully!")


if __name__ == "__main__":
    build_rag()