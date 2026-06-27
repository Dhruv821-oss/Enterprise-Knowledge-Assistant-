from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

SUPPORTED_EXTENSIONS = [".pdf"]


def load_documents(path: str):
    """
    Load documents from either:
    - A single PDF file
    - A directory containing PDFs

    Returns:
        List[Document]
    """

    documents = []

    path = Path(path)

    # --------------------------
    # Single PDF
    # --------------------------
    if path.is_file():

        if path.suffix.lower() in SUPPORTED_EXTENSIONS:

            print(f"Loading {path.name}")

            loader = PyMuPDFLoader(str(path))

            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = path.name

            documents.extend(docs)

        return documents

    # --------------------------
    # Directory of PDFs
    # --------------------------
    if path.is_dir():

        for file_path in path.rglob("*"):

            if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            print(f"Loading {file_path.name}")

            loader = PyMuPDFLoader(str(file_path))

            docs = loader.load()

            for doc in docs:
                doc.metadata["source"] = file_path.name

            documents.extend(docs)

        return documents

    raise FileNotFoundError(f"{path} does not exist.")