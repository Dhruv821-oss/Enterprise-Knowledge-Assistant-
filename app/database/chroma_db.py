from langchain_chroma import Chroma

VECTOR_DB_PATH = "vector_store"


def load_vector_store(embeddings):
    return Chroma(
        persist_directory=VECTOR_DB_PATH,
        embedding_function=embeddings
    )


def add_documents(chunks, embeddings):
    db = load_vector_store(embeddings)
    db.add_documents(chunks)
    return db