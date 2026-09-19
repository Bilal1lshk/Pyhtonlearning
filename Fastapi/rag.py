from langchain_core.documents import Document
doc=Document(page_content="This is a sample document.", metadata={"source": "sample_source"})
print(doc)