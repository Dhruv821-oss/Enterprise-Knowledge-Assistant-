from app.rag.assistant import EnterpriseAssistant

assistant = EnterpriseAssistant()

while True:

    question = input("\nAsk a question (or type 'exit'): ")

    if question.lower() == "exit":
        break

    result = assistant.ask(question)

    print("\nAnswer:\n")
    print(result["answer"])

    print("\nConfidence:")
    print(result["confidence"])

    print("\nSources:")

    for source in result["sources"]:
        print(
            f"- {source['document']} (Page {source['page']})"
        )