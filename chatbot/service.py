from google import genai
from django.conf import settings
from .prompts import SYSTEM_PROMPT


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def generate_response(prompt):

    final_prompt = f"""
    {SYSTEM_PROMPT}

    User:
    {prompt}
    """


    response = client.models.generate_content(
        
        model="gemini-3.5-flash",
        contents=final_prompt
    )
    return response.text