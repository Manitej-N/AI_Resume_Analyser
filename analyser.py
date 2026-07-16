import os
import json
from google import genai
from google.genai.errors import ServerError
from dotenv import load_dotenv

load_dotenv('.env')
key = os.getenv("GOOGLE_API_KEY") 
client = genai.Client(api_key=key)

def call_model(prompt):
    try:
        output = client.models.generate_content(model="gemini-3.5-flash", contents= prompt)
        return output.text
    except ServerError:
        print('Server Error, please try again' )
        return '{"error": "Server busy, please try again"}'
