import os

from django.shortcuts import render
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def chat(request):

    user_message = ""
    ai_response = ""

    if request.method == "POST":

        user_message = request.POST.get("message")

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=user_message,
        )

        ai_response = response.text

    context = {
        "user_message": user_message,
        "ai_response": ai_response,
    }

    return render(request, "chatbot/chat.html", context)