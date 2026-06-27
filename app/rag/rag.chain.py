from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from app.rag.embeddings import get_embedding_model
from app.database.chroma_db import load_vector_store
from langchain_ollama import ChatOllama


def build_rag_chain():

    embeddings = get_embedding_model()

    vectordb = load_vector_store(embeddings)

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 4}
    )

    llm = ChatOllama(
        model="llama3.2",      # Change if needed
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an Enterprise Knowledge Assistant.

Use ONLY the provided context to answer.

If the answer is unavailable, say:
"I couldn't find this information in the knowledge base."

Context:
{context}

Question:
{input}
"""
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    rag_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return rag_chain