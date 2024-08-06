from crewai import Agent, Task, Crew, Process
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

search_tool = DuckDuckGoSearchRun() 

# Create the DuckDuckGo search agent
search_agent = Agent(
    role="price agent",
    goal="Find the most relevant price information on a travel trip for {place1} and {place2}",
    backstory="You are an expert at using DuckDuckGo to search for information on a wide range of topics and return a summary.",
    tools=[search_tool],
    llm=llm,
)

# Create the price comparison agent
price_agent = Agent(
    role="Price Comparison Agent",
    goal="Show all prices from booking to billing for two places",
    backstory="You are an experienced price comparison agent who can find and compare prices for various products and services.",
    llm=llm,
)

# Create the search task
search_task = Task(
    description="""
    Search for information on price comparison for {place1} and {place2}
    Return a summary of the most relevant information found in markdown format:
    1. Flight
    2. Hotel
    3. Car
    4. Booking
    """,
    expected_output="A summary of the most relevant information found",
    agent=search_agent,
)

# Create the price comparison task
price_task = Task(
    description="Compare the summary and display the report for {place1} and {place2}",
    expected_output="A comparison report of prices for the two places, including booking and billing costs",
    agent=price_agent,
    output_file="price_comparison.md",
)

# Create the crew
crew = Crew(
    agents=[search_agent, price_agent],
    tasks=[search_task, price_task],
    process=Process.sequential, 
    verbose=2
)

# Kick off the crew
result = crew.kickoff(inputs={"place1": "New York", "place2": "London"})

# Print the result
print(result)