from crewai import Task, Crew
from classes.email_agent import email_agent

# Create a task for generating the email
generate_email_task = Task(
    description="Generate an email explaining the medical note, patient details, and doctor name",
    expected_output="Generated email as a string",
    agent=email_agent,
    output_file="email.md"
)

# Create a crew for executing tasks
email_crew = Crew(
    agents=[email_agent],
    tasks=[generate_email_task],
    verbose=2
)