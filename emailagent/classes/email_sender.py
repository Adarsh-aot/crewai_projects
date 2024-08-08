import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize email credentials
email_password = os.getenv('EMAIL_PASSWORD')
sender_email = os.getenv('SENDER_EMAIL')

def send_email(recipient_email: str, subject: str, message: str) -> str:
    """Send an email to the specified recipient."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email. Error: {str(e)}"

def generate_email_subject(content: str) -> str:
    """Generate an email subject based on the provided content."""
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Generate an email subject for the following content: {content}"
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content