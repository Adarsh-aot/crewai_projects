import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
import json
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize the language model
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    api_key=os.getenv("GROQ_API_KEY"),
)

# Initialize email credentials
email_password = os.getenv('EMAIL_PASSWORD')
sender_email = os.getenv('SENDER_EMAIL')

# Function to send email
def send_email(recipient_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.close()
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email. Error: {str(e)}"

# Create an agent for generating email content
email_agent = Agent(
    role='Medical Note Explainer',
    goal='Generate an email explaining the provided medical note ({medical_note}), patient details ({patient_details}), and doctor name ({doctor_name})',
    backstory='You are an AI-powered medical note explainer. Your job is to create a clear and concise email explaining the medical note to the recipient.',
    verbose=True,
    llm=llm
)

# Create a task for generating the email
generate_email_task = Task(
    description="Generate an email explaining the medical note, patient details, and doctor name",
    expected_output="Generated email as a string",
    agent=email_agent ,
    output_file="email.md"
)

# Create a crew for executing tasks
email_crew = Crew(
    agents=[email_agent],
    tasks=[generate_email_task],
    verbose=2
)

# Run the crew with the medical note, patient details, and doctor name
result = email_crew.kickoff(
    {
        "medical_note": "This is a reminder for your upcoming appointment.",
        "patient_details": "Kesav Gopan, AOT Technologies, Trivandrum",
        "doctor_name": "Dr. John"
    }
)

# Generate the email subject
def generate_subject(message):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Generate an email subject for the following content: " + message
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

# Print the result
print(result)

# Example usage for sending the email
recipient_email = "kesav.gopan@aot-technologies.com"
subject = generate_subject("This is a reminder for your upcoming appointment.")

# Access the generated email content
generated_email = str(result)

if generated_email:
    # Send the email
    email_result = send_email(recipient_email, subject, generated_email)
    print(email_result)
else:
    print("Failed to generate the email content.")