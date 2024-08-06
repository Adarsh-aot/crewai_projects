# agent.py
from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the language model
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Create the quote research agent
quote_research_agent = Agent(
    role="Quote Research Agent",
    goal="Find the most relevant quote from the specified book({book_title}) that relates to the given topic({topic})",
    backstory="You are an expert at researching and analyzing quotes from books to find the most relevant ones for a given topic.",
    llm=llm,
)

# Create the quote explanation agent
quote_explanation_agent = Agent(
    role="Quote Explanation Agent",
    goal="Explain how the given quote relates to your life and provide actionable insights",
    backstory="You are an experienced life coach who can provide insightful explanations on how quotes from books can be applied to one's life.",
    llm=llm,
)

# Export agents
def get_agents():
    return quote_research_agent, quote_explanation_agent