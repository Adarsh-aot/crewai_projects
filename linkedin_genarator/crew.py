from crewai import Agent, Task, Crew, Process
from crewai_tools import tool
from langchain_groq import ChatGroq
import os
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
load_dotenv()

@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic"""
    return DuckDuckGoSearchRun().run(search_query)


# Initialize the language model
llm =  ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),              
)


linkedin_agent = Agent(
    role="LinkedIn Generator",
    goal="Generate one LinkedIn post idea from internet search results for the following content: {content}",
    backstory="You are an expert at generating LinkedIn post ideas.",
    tools = [search],
    llm = llm
)

content_agent = Agent(
    role="Content Generator",
    goal="Generate a LinkedIn post from given post idea",
    backstory="You are an expert at generating LinkedIn post .",
    llm = llm
)


linked_task = Task(
    description="Generate a LinkedIn post idea from internet search results for the following content: {content}",
    expected_output = "linkedin post idea",
    agent = linkedin_agent
)


content_task = Task(
    description="Generate a LinkedIn post from given post idea",
    expected_output = "linkedin post",
    agent = content_agent ,
    output_file = "linkedin.md"
)



crew = Crew(
    agents=[linkedin_agent, content_agent],
    tasks=[linked_task, content_task],
    process=Process.sequential,
    verbose=2
)


data = input("Enter the content: ")
result = crew.kickoff({"content": data})    
print(result)