import os
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    output = response.text
    return output

if __name__ == "__main__":
    while True:
        user_query = input("Enter your prompt (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        response = generate_response(user_query)
        print("AI Response:", response)