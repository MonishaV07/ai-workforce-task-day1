from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"


# Custom Model 1: College Fee Assistant
fee_system_prompt = """
You are a college fee assistant for the Department of AI and Data Science.

Never guess a fee.
If the required fee information is not provided, say that you need to look it up.

Answer in one short sentence.
"""


# Custom Model 2: Events Announcer
events_system_prompt = """
You are a college events announcement assistant.

Write short, clear and engaging announcements
for college events.

Include the event name, date, time and venue
when those details are provided.
"""


def ask_model(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content


print("=" * 60)
print("CUSTOM MODEL 1 - FEE ASSISTANT")
print("=" * 60)

print(
    ask_model(
        fee_system_prompt,
        "What is the semester fee?"
    )
)


print("\n" + "=" * 60)
print("CUSTOM MODEL 2 - EVENTS ANNOUNCER")
print("=" * 60)

print(
    ask_model(
        events_system_prompt,
        "Create an announcement for an AI Hackathon on October 15 at 10 AM in the Seminar Hall."
    )
)