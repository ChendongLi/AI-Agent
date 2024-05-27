from langchain_google_vertexai import ChatVertexAI
from pathlib import Path
from langchain.prompts import load_prompt
from langchain.output_parsers.json import SimpleJsonOutputParser
from langsmith.wrappers import wrap_openai

current_dir = Path(__file__)
current_directory_name = current_dir.parts[-2]
root_dir = [p for p in current_dir.parents if p.name ==
            current_directory_name][0]

llm = ChatVertexAI(model="gemini-pro")
prompt_template = load_prompt(f"{root_dir}/config/prompt.yaml")

# prompt = prompt_template.format(
#     inputs="Who is current US president?", users='someone')


# print(prompt)

# response = llm.invoke(prompt)

json_parser = SimpleJsonOutputParser()

json_chain = prompt_template | llm | json_parser


print(json_chain.invoke(
    {"inputs": "Who is current US president?", "users": 'someone'}))
