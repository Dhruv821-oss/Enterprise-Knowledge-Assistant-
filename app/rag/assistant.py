from langchain_ollama import ChatOllama

from app.rag.hybrid_retriever import HybridRetriever
from app.rag.prompts import QA_PROMPT


class EnterpriseAssistant:
    """
    Enterprise Knowledge Assistant

    Pipeline:
    User Query
        ↓
    Hybrid Retrieval (BM25 + Vector)
        ↓
    Reciprocal Rank Fusion
        ↓
    CrossEncoder Reranking
        ↓
    Ollama LLM
        ↓
    Answer + Sources + Confidence
    """

    def __init__(self):

        self.retriever = HybridRetriever()

        self.llm = ChatOllama(
            model="llama3.2",      # Change if using another model
            temperature=0,
        )

    def ask(self, question: str):

        # Retrieve top documents
        docs = self.retriever.retrieve(question)

        # Build context
        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        # Build prompt
        prompt = QA_PROMPT.format(
            context=context,
            question=question
        )

        # Generate answer
        response = self.llm.invoke(prompt)

        # Collect unique sources
        seen = set()
        sources = []

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

        # Temporary confidence
        confidence = round(
            min(0.99, 0.75 + (0.05 * len(sources))),
            2
        )

        return {
            "question": question,
            "answer": response.content,
            "sources": sources,
            "confidence": confidence
        }