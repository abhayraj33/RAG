from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("docs\Brijesh Kumar - Resume (5).pdf")
docs = loader.load()

spliter=CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

result=spliter.split_documents(docs)

print(result)