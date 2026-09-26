from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



loader=TextLoader("Poem.txt",encoding="utf-8")

docs=loader.load()

llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    provider="auto",
    temperature=0.8
)

model=ChatHuggingFace(llm=llm)
parser=StrOutputParser()

prompt=PromptTemplate(
    template="Write a appropriate summaary on  the given poem \n {poem}",
    input_variables=["poem"]
)

chain= prompt | model | parser

print(chain.invoke({"poem":docs[0].page_content}))

