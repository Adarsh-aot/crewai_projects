# task.py
from crewai import Task
from agent import get_agents
# Create the quote research task

quote_research_agent, quote_explanation_agent = get_agents()
quote_research_task = Task(
    description="""
    Research the specified book and find the most relevant quote that relates to the given topic.
    Return the quote, the book title, and the author's name in the following format:

    > "Quote" - Book Title by Author Name
    """,
    agent = quote_research_agent,
    expected_output="The most relevant quote from the specified book",
)

# Create the quote explanation task
quote_explanation_task = Task(
    description="Explain how the given quote relates to your life and provide actionable insights",
    agent = quote_explanation_agent ,
    expected_output="An explanation of how the quote relates to your life and actionable insights",
    output_file = "quote_explanation.md"
)

# Export tasks
def get_tasks():
    return quote_research_task, quote_explanation_task