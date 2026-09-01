import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# # Allow your Next.js frontend to call FastAPI
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "https://your-leadwise-domain.com",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Gemini client
client = genai.Client(
    api_key=os.getenv("gemini_api_key")
)


# Request body from Next.js
class ChatRequest(BaseModel):
    message: str


# Your AI tool
def get_weather(city: str):
    return f"The weather in {city} is 30°C and sunny."


tools = [get_weather]


@app.get("/")
def home():
    return {
        "message": "LeadWise AI API is running"
    }


@app.post("/ai/chat")
def chat(request: ChatRequest):

    chat = client.chats.create(
        model="gemini-3.6-flash",
        config={
            "tools": tools
        }
    )

    response = chat.send_message(
        request.message
    )

    return {
        "success": True,
        "response": response.text
    }