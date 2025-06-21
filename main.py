from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views.api import api

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",  # ✅ Allow Live Server frontend
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # ✅ Only allow frontend domain
    allow_credentials=True,
    allow_methods=["*"],             # ✅ Allow all methods (GET, POST, etc.)
    allow_headers=["*"],             # ✅ Allow all headers (Content-Type, etc.)
)

app.include_router(api)
