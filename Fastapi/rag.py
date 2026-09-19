import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import (
    TextLoader,
    PyMuPDFLoader,
    DirectoryLoader
)

loader = DirectoryLoader(
    path="./data",
    glob="**/*.pdf",
    loader_cls=PyMuPDFLoader,
    show_progress=True
)

pdf_docs = loader.load()
print(f"Total PDF pages loaded: {len(pdf_docs)}")

text_docs = TextLoader("text.txt", encoding="utf-8").load()
print(f"Text file loaded: {len(text_docs)} document(s)")