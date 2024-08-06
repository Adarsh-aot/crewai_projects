from crewai import Agent, Task, Crew
from crewai_tools import tool
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
load_dotenv()


# Initialize the language model
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)


