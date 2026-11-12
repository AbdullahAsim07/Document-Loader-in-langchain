from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model=ChatGroq(model='openai/gpt-oss-120b')
prompt=PromptTemplate(
    template='write down the summary of the following {text}',
    input_variables={"text"}
)
parser=StrOutputParser()
loader=TextLoader(
    file_path=("transformer_intro.txt")
)
#is ma docs ka nader loader ko save kar diya  aur jab document load hota as a list ma hota hai  
docs=loader.load()
print(docs)
print(type(docs))
# docs ki list dekhne ka liye 
print(len(docs))
# docs ki item  bhi nikalne ka liye 
print(type(docs[0]))
# metadata aur page content ka liye 
print(docs[0].metadata)
print(docs[0].page_content)
chain=prompt|model|parser
print(chain.invoke({'text':docs[0].page_content}))