import os

from django.shortcuts import render
from dotenv import load_dotenv
from google import genai

from .service import generate_response

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def chat(request):

    user_message = ""
    reply = ""


    if request.method == "POST":

        user_message = request.POST.get("message")

        reply = generate_response(user_message)

    return render(request, "chatbot/chat.html",  {"user_message": user_message,"reply":reply})