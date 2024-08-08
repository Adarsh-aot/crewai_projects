from crewai import Agent
from langchain_groq import ChatGroq
import os

# Initialize the language model
language_model = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Create an agent for generating email content
email_agent = Agent(
    role='Medical Note Explainer',
    goal='Generate an email explaining the provided medical note ({medical_note}), patient details ({patient_details}), and doctor name ({doctor_name})',
    backstory='You are an AI-powered medical note explainer. Your job is to create a clear and concise email explaining the medical note to the recipient.',
    verbose=True,
    llm=language_model
)

