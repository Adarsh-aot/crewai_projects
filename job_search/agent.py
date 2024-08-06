from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_community.tools.google_jobs import GoogleJobsQueryRun
from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper
from crewai import Agent, Task, Crew

# Load dotenv
load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Initialize the Google Jobs tool
google_jobs_tool = GoogleJobsQueryRun(api_wrapper=GoogleJobsAPIWrapper())

# Define the agent
employee_agent = Agent(
    role='Job Applicant',
    goal='Find job openings that match my skills and prepare for interviews',
    backstory="""You are an enthusiastic job applicant looking for positions that align with your skills and interests. Search for jobs using Google Jobs. You should return a maximum of 5 job openings. (return in the first try, don't repeat)""",
    verbose=True,
    allow_delegation=False,
    tools=[google_jobs_tool],
    llm=llm,
   
)

# Create the task
task3 = Task(
    description="""As a job applicant, inquire about job openings that match my skills and ask for tips on how to prepare for interviews effectively. Search for job openings using Google Jobs, but stop after 2 iterations.""",
    expected_output="A list of job recommendations and interview preparation tips.",
    agent=employee_agent,
)

# Instantiate the crew with a sequential process
crew = Crew(
    agents=[employee_agent],
    tasks=[task3],
    process="sequential",  # Ensuring the process is set to sequential
    verbose=True
)

# Kick off the crew to start on its tasks
preference = input("Enter your preference: ")
result = crew.kickoff({
    "preference": preference
})

print("######################")
print(result)
