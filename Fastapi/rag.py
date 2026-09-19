from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
documents = TextLoader("text.txt", encoding="utf-8").load()
print(documents)
