import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not set. "
        "Create a .env file and add your API key."
    )

MODEL = "qwen/qwen3.8-27b"
client = Groq(api_key=API_KEY)


def ask_llm(prompt, temperature=0.0):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature
    )

    return response.choices[0].message.content