import os
from langchain.chains import LLMChain
from langchain_community.llms import Minimax
from langchain_core.prompts import PromptTemplate
os.environ["MINIMAX_API_KEY"] = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJBbGVrc2V5IFl1cmNoZW5rbyIsIlVzZXJOYW1lIjoiQWxla3NleSBZdXJjaGVua28iLCJBY2NvdW50IjoiIiwiU3ViamVjdElEIjoiMTg3OTk1MTg0ODMzNzU3NjQ2NSIsIlBob25lIjoiIiwiR3JvdXBJRCI6IjE4Nzk5NTE4NDgzMzMzODIxNjEiLCJQYWdlTmFtZSI6IiIsIk1haWwiOiJhbXVybHlueEBnbWFpbC5jb20iLCJDcmVhdGVUaW1lIjoiMjAyNS0wMS0yMiAxMDoxNzoxOSIsIlRva2VuVHlwZSI6MSwiaXNzIjoibWluaW1heCJ9.TO9lh03nCcOENY1LGT_ibcVuRN8V5SX-xq72iiubo_teiHC1qmAXhhFZIiR3DkivnDurz_HXGw1GAgM18BBI6QITNZ8iU3tuyaCbaOEpqoh1QvjfaC6XvVzHvOLoxHWbumzbH7Gh98hWDar3WZzz_vFgaHv_h7z96PrqQ2HaUzQeDSZxqR1E9Osuls8CJg3dBGYrPsImK9t68Ie_tVlZRkFiFbp_dobSVLTpZCXidVDwbvVrD7kFsrl9t3SgkRD3z7byst4C_Xl6bNnf0slOakX62qobeRpcq0OvwchQ4XyNdJi4IhpnQPu04bdkIx_AVHscenECaFWxu2BCrImSkg"
os.environ["MINIMAX_GROUP_ID"] = "1879951848333382161"
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