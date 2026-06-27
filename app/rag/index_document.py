from app.utils.loaders import load_documents
from app.rag.chunking import chunk_documents
from app.rag.embeddings import get_embedding_model
from app.database.chroma_db import add_documents


def index_document(file_path):

    docs = load_documents(file_path)

    chunks = chunk_documents(docs)

    embeddings = get_embedding_model()

    add_documents(chunks, embeddings)

    print("Document indexed successfully.")