# # views/api.py
# from fastapi import APIRouter
# from pydantic import BaseModel
# from fastapi.responses import JSONResponse
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# # Load .env file
# load_dotenv()

# api = APIRouter()  # ✅ This must exist!

# # Fetch API key from environment
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel('models/gemini-1.5-flash')

# class EmailInput(BaseModel):
#     email: str
#     tone: str

# @api.post("/generate")
# async def generate_email(input_data: EmailInput):
#     prompt = f"""Carefully read the email provided below and draft a well-structured response in a {input_data.tone} tone, ensuring clarity, professionalism, and alignment with the original message's context:
    
#     Email:
#     {input_data.email}
#     """
#     try:
#         response = model.generate_content(prompt)
#         reply = response.text if hasattr(response, 'text') else response['text']
#         return JSONResponse(content={"reply": reply})
#     except Exception as e:
#         return JSONResponse(content={"reply": "Something went wrong."}, status_code=500)






from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import google.generativeai as genai
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

api = APIRouter()

# Google API Configuration
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-flash')

class EmailInput(BaseModel):
    email: str
    tone: str

class SendEmailInput(BaseModel):
    to_email: str
    subject: str
    body: str

@api.post("/generate")
async def generate_email(input_data: EmailInput):
    prompt = f"""Carefully read the email provided below and draft a well-structured response in a {input_data.tone} tone, ensuring clarity, professionalism, and alignment with the original message's context:

    Email:
    {input_data.email}
    """
    try:
        response = model.generate_content(prompt)
        reply = response.text if hasattr(response, 'text') else response['text']
        return JSONResponse(content={"reply": reply})
    except Exception as e:
        return JSONResponse(content={"reply": "Something went wrong."}, status_code=500)

@api.post("/send-email")
async def send_email(data: SendEmailInput):
    try:
        sender_email = os.getenv("SMTP_EMAIL")
        sender_password = os.getenv("SMTP_PASSWORD")

        print("📨 Sending from:", sender_email)
        print("🔑 Password exists:", bool(sender_password))
        print("📩 To:", data.to_email)
        print("📌 Subject:", data.subject)
        print("📄 Body:", data.body)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = data.to_email
        msg['Subject'] = data.subject
        msg.attach(MIMEText(data.body, 'plain'))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, data.to_email, msg.as_string())

        return JSONResponse(content={"message": "✅ Email sent successfully!"})

    except Exception as e:
        import traceback
        traceback.print_exc()  # prints to terminal
        return JSONResponse(content={"message": f"❌ Internal Server Error: {str(e)}"}, status_code=500)
