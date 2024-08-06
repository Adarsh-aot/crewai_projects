from crewai import Agent, Task, Crew
from crewai_tools import tool
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
load_dotenv()

@tool('DuckDuckGoSearch')
def search(search_query: str):
    """Search the web for information on a given topic"""
    return DuckDuckGoSearchRun().run(search_query)


# Initialize the language model
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Function to perform Google search

# Define the Researcher agent
researcher = Agent(
    role='Researcher',
    goal='Gather comprehensive and accurate information on the given topic({topic})',
    backstory='You are an expert researcher with a keen eye for detail and the ability to find reliable sources quickly.',
    verbose=True,
    allow_delegation=False,
    tools=[search],
    llm=llm
)

# Define the Writer agent
writer = Agent(
    role='Writer',
    goal='Create an engaging and informative newsletter based on the research provided',
    backstory='You are a skilled writer with a talent for explaining complex topics in an accessible and interesting way.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define the tasks
research_task = Task(
    description='Research the given topic thoroughly. Gather key facts, recent developments, and interesting angles.',
    expected_output = "detailed report on the topic",
    agent=researcher
)

writing_task = Task(
    description='Using the research provided, write an engaging newsletter article on the topic. Include an attention-grabbing headline, key points, and a conclusion.',
    expected_output = "newsletter article",
    agent=writer,
    output_file = "newsletter.md"
)

# Create the crew
newsletter_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    verbose=2
)

# Run the crew
result = newsletter_crew.kickoff({
    'topic': 'The Future of AI: Trends and Predictions'
    })

