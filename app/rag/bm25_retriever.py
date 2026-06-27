from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self, documents):
        self.documents = documents

        self.corpus = [
            doc.page_content.split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(self.corpus)

    def retrieve(self, query, k=10):

        tokens = query.split()

        docs = self.bm25.get_top_n(
            tokens,
            self.documents,
            n=k
        )

        return docs