from pydantic import BaseModel

class EmailRequest(BaseModel):
    medical_note: str = "This is a reminder for your upcoming appointment on April 15, 2024, at 10:00 AM."
    patient_details: str = "Kesav Gopan, AOT Technologies, Trivandrum, Kerala, India."
    doctor_name: str = "Dr. John Smith"
    recipient_email: str = "kesav.gopan@aot-technologies.com"