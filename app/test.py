from app.rag.qa import EnterpriseQA

assistant = EnterpriseQA()

question = input("Ask a question: ")

result = assistant.ask(question)

print("\nAnswer:\n")
print(result["answer"])

print("\nSources:\n")

for src in result["sources"]:
    print(src)