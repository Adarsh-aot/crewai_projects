from pydantic import BaseModel

class EmailResponse(BaseModel):
    message: str
    recipient_email: str
    subject: str
    email_content: str = "Dear Kesav Gopan,\n\nThis is a reminder for your upcoming appointment on April 15, 2024, at 10:00 AM.\n\nBest regards,\nDr. John Smith"