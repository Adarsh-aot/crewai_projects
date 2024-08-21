from crewai import Agent, Task, Crew, Process
import os
import json
from crewai_tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun

# Load environment variables from .env file
load_dotenv()

@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic using DuckDuckGo."""
    return DuckDuckGoSearchRun().run(search_query)

# Initialize the language model
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Create the DuckDuckGo search agent
search_agent = Agent(
    role="calorie agent", 
    goal="create a list food item name based on a given amount of calories ({calory}) with ditory preference({dpreff}) and prefered cuisine({cuisine}).",
    backstory="You are an expert at information on a wide range of food items ",
    llm=llm,
)

# Define the search task
search_task = Task(
    description="Find the most relevant food item based on a given amount of calories ({calory}).",
    expected_output="food item in array of json format with name,calories,ingredients  ( only array of json  no string )", 
    agent=search_agent,
    output_file="calory.md"
)

# Create the Crew with the agent and task
crew = Crew(
    agents=[search_agent],
    tasks=[search_task],
    process=Process.sequential,
    verbose=2
)

# Execute the Crew with a specified calorie input
calory = input("Enter  calorie amount to take ")
dpreff = input("Enter  directory preference   ")
cuisine = input("Enter  cuisine     ") 
result = crew.kickoff(inputs={"calory": calory  , "dpreff": dpreff, "cuisine": cuisine})
   
# Print the result
print(json.loads(str(result)[4:-4]))