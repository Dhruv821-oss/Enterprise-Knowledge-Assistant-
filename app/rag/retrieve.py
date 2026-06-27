from app.rag.embeddings import get_embedding_model
from app.database.chroma_db import load_vector_store


class VectorRetriever:
    """
    Semantic vector retriever using ChromaDB and MMR.
    """

    def __init__(self):
        embeddings = get_embedding_model()
        self.db = load_vector_store(embeddings)

    def retrieve(self, query: str, k: int = 10):
        retriever = self.db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": k,
                "fetch_k": 20,
            },
        )

        return retriever.invoke(query)

    def retrieve_with_scores(self, query: str, k: int = 10):
        return self.db.similarity_search_with_score(
            query,
            k=k,
        )