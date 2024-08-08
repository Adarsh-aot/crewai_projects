from fastapi import FastAPI , Body
from classes.email_request import EmailRequest
from classes.email_response import EmailResponse
from classes.email_sender import send_email , generate_email_subject
from classes.email_agent import email_agent
from classes.email_crew import email_crew

app = FastAPI()

@app.post("/generate_email", response_model=EmailResponse, summary="Generate an email based on the provided medical note, patient details, and doctor name")
def generate_email(request: EmailRequest = Body(..., example={
    "medical_note": "This is a reminder for your upcoming appointment on April 15, 2024, at 10:00 AM.",
    "patient_details": "Kesav Gopan, AOT Technologies, Trivandrum, Kerala, India.",
    "doctor_name": "Dr. John Smith",
    "recipient_email": "kesav.gopan@aot-technologies.com"
})):
    """Generate an email based on the request data."""
    # Run the crew with the provided data
    result = email_crew.kickoff(
        {
            "medical_note": request.medical_note,
            "patient_details": request.patient_details,
            "doctor_name": request.doctor_name
        }
    )

    # Access the generated email content
    generated_email = str(result)

    if generated_email:
        # Generate the email subject
        subject = generate_email_subject(request.medical_note)

        return {
            "message": "Email generated successfully.",
            "recipient_email": request.recipient_email,
            "subject": subject,
            "email_content": generated_email
        }
    else:
        return {"message": "Failed to generate the email content."}

@app.post("/send_email", summary="Send the generated email", response_model=EmailResponse)
def send_email_endpoint(request: EmailResponse = Body(..., example={
    "message": "Email sent successfully.",
    "recipient_email": "kesav.gopan@aot-technologies.com",
    "subject": "Reminder for Upcoming Appointment",
    "email_content": "Dear Kesav Gopan,\n\nThis is a reminder for your upcoming appointment on April 15, 2024, at 10:00 AM.\n\nBest regards,\nDr. John Smith"
})):
    """Send the generated email."""
    # Send the email    
    email_result = send_email(request.recipient_email, request.subject, request.email_content)
    
    # Return a complete response
    return {
        "message": email_result,
        "recipient_email": request.recipient_email,
        "subject": request.subject,
        "email_content": request.email_content
    }