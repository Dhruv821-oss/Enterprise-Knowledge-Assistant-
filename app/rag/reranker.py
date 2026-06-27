from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query, docs, top_k=5):

        pairs = [
            (query, doc.page_content)
            for doc in docs
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(scores, docs),
            reverse=True,
            key=lambda x: x[0]
        )

        return [
            doc
            for _, doc in ranked[:top_k]
        ]