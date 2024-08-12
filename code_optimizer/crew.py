from crewai  import Agent , Task , Crew , Process 
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


code_optimizer = Agent(
    role="Code Optimizer",
    goal="Optimize the code({code}) to make it more efficient and readable",
    backstory="You are an expert at optimizing code to make it more efficient and readable.",
    llm = llm 
)

code_suggestion = Agent(
    role="Code Suggestion",
    goal="Suggest code changes to make the code({code}) more efficient and readable",
    backstory="You are an expert at suggesting code changes to make the code({code}) more efficient and readable.",
    llm = llm       
)

code_opt_task = Task(
    description="Optimize the code({code}) to make it more efficient and readable",
    expected_output="The code({code}) has been optimized to make it more efficient and readable",
    agent=code_optimizer,
    output_file="code_opt.md"
)


code_sug_task = Task(
    description="Suggest code changes to make the code({code}) more efficient and readable",
    expected_output="The code({code}) has been optimized to make it more efficient and readable",
    agent=code_suggestion,
    output_file="code_sug.md"
)


crew = Crew(
    agents=[code_optimizer, code_suggestion],
    tasks=[code_opt_task, code_sug_task],
    process=Process.sequential,
    verbose=2
)

data = input("Enter the code: ")
result = crew.kickoff({"code": data})

print(result)


