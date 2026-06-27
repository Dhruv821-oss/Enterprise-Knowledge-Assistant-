from langchain_ollama import ChatOllama

from app.rag.prompts import QA_PROMPT


class AnswerGenerator:

    def __init__(self):
        self.llm = ChatOllama(
            model="llama3.2",   # Change if you downloaded a different model
            temperature=0
        )

    def generate(self, question, docs):
        context = "\n\n".join(doc.page_content for doc in docs)

        prompt = QA_PROMPT.format(
            context=context,
            question=question
        )

        response = self.llm.invoke(prompt)

        return response.content