from app.utils.loaders import load_documents
from app.rag.chunking import chunk_documents
from app.rag.bm25_retriever import BM25Retriever
from app.rag.retrieve import VectorRetriever
from app.rag.rrf import reciprocal_rank_fusion
from app.rag.reranker import Reranker


class HybridRetriever:

    def __init__(self):

        docs = load_documents("app/data/documents")

        chunks = chunk_documents(docs)

        self.bm25 = BM25Retriever(chunks)

        self.vector = VectorRetriever()

        self.reranker = Reranker()

    def retrieve(self, query):

        bm25_docs = self.bm25.retrieve(query)

        vector_docs = self.vector.retrieve(query)

        fused = reciprocal_rank_fusion([
            bm25_docs,
            vector_docs
        ])

        reranked = self.reranker.rerank(
            query,
            fused,
            top_k=5
        )

        return reranked