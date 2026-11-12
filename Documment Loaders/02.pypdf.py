from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
loader=PyPDFLoader("ml.pdf")
loader.load()
docs=loader.load()
print(docs)
print(len(docs))
print(docs[0].metadata)
print(docs[1].page_content)