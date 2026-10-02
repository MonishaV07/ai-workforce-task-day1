from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": """
You are a pirate.
Answer every question in a short pirate-style sentence.
"""
        },
        {
            "role": "user",
            "content": "What is an AI agent?"
        }
    ]
)

print(response.choices[0].message.content)