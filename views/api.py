# views/api.py
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

api = APIRouter()  # ✅ This must exist!

# Fetch API key from environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('models/gemini-1.5-flash')

class EmailInput(BaseModel):
    email: str
    tone: str

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
