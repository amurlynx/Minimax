import os
from langchain.chains import LLMChain
from langchain_community.llms import Minimax
from langchain_core.prompts import PromptTemplate
os.environ["MINIMAX_API_KEY"] = ""
os.environ["MINIMAX_GROUP_ID"] = ""
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

llm = Minimax(
    minimax_api_key=os.environ["MINIMAX_API_KEY"],
    minimax_group_id=os.environ["MINIMAX_GROUP_ID"]
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NBA team won the Championship in the year Jay Zhou was born?"

llm_chain.invoke(question)
