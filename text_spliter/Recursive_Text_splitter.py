from unittest import loader, result
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import TextLoader

load=TextLoader("docs\Poem.txt",encoding="utf-8")

docs=load.load()


splitter=RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=0
)

result=splitter.split_documents(docs)

print(result)