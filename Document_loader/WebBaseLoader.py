# from html import parser
# from itertools import chain
# from tempfile import template
# from urllib.request import URLopener
# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers  import StrOutputParser
# from dotenv import load_dotenv

# from langchain_community.document_loaders import WebBaseLoader

# URL="https://www.amazon.in/Google-Pixel-8a-Aloe-128/dp/B0DTKC2HXV/ref=pd_rhf_dp_s_pd_sbs_rvi_d_sccl_1_3/522-7037824-2234748?pd_rd_w=9jcjo&content-id=amzn1.sym.ed04a9b6-f1e8-467f-8e81-e050db1b5151&pf_rd_p=ed04a9b6-f1e8-467f-8e81-e050db1b5151&pf_rd_r=0ZYK8JVP6ENM9RG4JSPR&pd_rd_wg=T3R9P&pd_rd_r=6aca04e2-9a4e-445a-9204-a3e4da7f7fb4&pd_rd_i=B0DTKC2HXV&psc=1https://www.flipkart.com/google-pixel-10a-fog-256-gb/p/itmeaa46d52e228a?pid=MOBHP6CEG7VDZHSW&lid=LSTMOBHP6CEG7VDZHSWDTANPD&marketplace=FLIPKART&q=pixel+8a&store=tyy%2F4io&srno=s_1_10&otracker=search&otracker1=search&fm=organic&iid=2d602278-18a0-4d6a-b3b7-60349b4214a9.MOBHP6CEG7VDZHSW.SEARCH&ppt=hp&ppn=homepage&ssid=o807tv66xc0000001790311871258&qH=8176b07c5ef8105a&ov_redirect=true"


# llm=HuggingFaceEndpoint(
#     repo_id="openai/gpt-oss-120b",
#     task="text-generation",
#     provider="auto"
# )

# model=ChatHuggingFace(llm=llm)

# prompt=PromptTemplate(
#     template="This is all the information \n {info} \n according to all the info provided tell give me your suggestion about the camera queality of this product",
#     input_variables=["info"]
# )




# parser=StrOutputParser()
# web_loader =WebBaseLoader(URL)

# loader=web_loader.load()

# chain=prompt | model | parser 

# result=chain.invoke({"info":loader[0].page_content})
# print(result)

