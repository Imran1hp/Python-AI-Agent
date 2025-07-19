from langchain_community.tools import WikipediaQueryRun,DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

def save_to_txt (data:str,filename:str="research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    formate_text =f"---Research Output --- \n {timestamp} \n\n {data}\n\n"
save_tool = Tool(
    name="Save",
    func=save_to_txt,
    description="Save the output to a text file",
)
search =DuckDuckGoSearchRun()
search_tool = Tool(
    name="Search",
    func=search.run,
    description="Search the web for infromation",
)


api_wrapper =WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=100)
wiki_tool =WikipediaQueryRun(api_wrapper=api_wrapper)