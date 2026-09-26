from ast import parse
from tempfile import template
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
doc_loader=doc_loader.load()


llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    provider="auto"

)
parser=StrOutputParser()


model=ChatHuggingFace(llm=llm)


prompt=PromptTemplate(
    template="this is a detailed notes \n {notes} give important point as bullet point that feels important",
    input_variables=['notes']
)


chain=prompt | model | parser

result=chain.invoke({"notes":docs[5].page_content})

# print(result)

print(doc_loader[96].page_content)