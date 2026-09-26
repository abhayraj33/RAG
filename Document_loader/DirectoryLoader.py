from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers  import StrOutputParser
from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv


loader=PyPDFLoader("Statics Interview Question5 (AutoRecovered).pdf")

docs=loader.load()

doc_loader=DirectoryLoader(
    path="docs",
    glob="*.pdf",
    loader_cls=PyPDFLoader

)
# doc_loader=doc_loader.load()

# print(doc_loader[0].page_content)

doc_loader=list(doc_loader.lazy_load())

print(doc_loader[0].page_content)

