import os
from google import genai
from dotenv import load_dotenv
load_dotenv('.env')
key = os.getenv("GOOGLE_API_KEY") 
client = genai.Client(api_key=key)
def call_model(prompt):
    output = client.models.generate_content(model="gemini-3.5-flash", contents= prompt)
    return output.text
print(call_model("say hello"))
