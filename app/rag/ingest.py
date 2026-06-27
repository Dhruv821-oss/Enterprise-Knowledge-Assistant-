from app.utils.loaders import load_documents
from app.rag.chunking import chunk_documents
from app.rag.embeddings import get_embedding_model
from app.database.chroma_db import create_vector_store


def ingest():

    print("Loading documents...")
    docs = load_documents("app/data/documents")

    print(f"{len(docs)} pages loaded")

    print("Chunking...")
    chunks = chunk_documents(docs)

    print(f"{len(chunks)} chunks created")

    print("Loading embedding model...")
    embeddings = get_embedding_model()

    print("Creating vector database...")
    create_vector_store(chunks, embeddings)

    print("Done!")


if __name__ == "__main__":
    ingest()