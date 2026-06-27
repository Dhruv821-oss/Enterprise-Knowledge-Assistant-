from app.rag.retrieve import Retriever
from app.rag.generator import AnswerGenerator


class EnterpriseQA:

    def __init__(self):
        self.retriever = Retriever()
        self.generator = AnswerGenerator()

    def ask(self, question):

        docs = self.retriever.retrieve(question)

        answer = self.generator.generate(question, docs)

        sources = []

        seen = set()

        for doc in docs:

            source = (
                doc.metadata.get("source"),
                doc.metadata.get("page")
            )

            if source not in seen:
                seen.add(source)

                sources.append({
                    "document": source[0],
                    "page": source[1]
                })

        return {
            "answer": answer,
            "sources": sources
        }