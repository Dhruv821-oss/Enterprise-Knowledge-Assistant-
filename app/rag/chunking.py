from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    """
    Split documents into overlapping chunks while preserving metadata.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=180,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            ""
        ]
    )

    chunks = splitter.split_documents(documents)

    return chunks