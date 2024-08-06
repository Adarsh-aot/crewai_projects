# crew.py
from crewai import Crew, Process
from agent import get_agents
from task import get_tasks

# Get agents and tasks
quote_research_agent, quote_explanation_agent = get_agents()
quote_research_task, quote_explanation_task = get_tasks()

# Create the crew
crew = Crew(
    agents=[quote_research_agent, quote_explanation_agent],
    tasks=[quote_research_task, quote_explanation_task],
    process=Process.sequential,
    verbose=2
)

# Kick off the crew
def run_crew(book_title, topic):
    result = crew.kickoff(inputs={"book_title": book_title, "topic": topic})
    return result

if __name__ == "__main__":
    # Example execution
    book_title = input("Enter the title of the book: ")
    topic = input("Enter the topic: ")
    output = run_crew(book_title , topic)
    print(output)

    