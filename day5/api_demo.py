from openai import OpenAI
import os
import time
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "openai/gpt-oss-20b"


# --------------------------------------------------
# 1. List available models
# --------------------------------------------------

print("=" * 60)
print("1. AVAILABLE MODELS")
print("=" * 60)

models = client.models.list()

for model in models.data:
    print(model.id)


# --------------------------------------------------
# 2. Normal chat completion
# --------------------------------------------------

print("\n" + "=" * 60)
print("2. NORMAL CHAT COMPLETION")
print("=" * 60)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "What is an AI agent?"
        }
    ]
)

print(response.choices[0].message.content)

if response.usage:
    print("\nPrompt tokens:", response.usage.prompt_tokens)
    print("Completion tokens:", response.usage.completion_tokens)
    print("Total tokens:", response.usage.total_tokens)


# --------------------------------------------------
# 3. Streaming + TTFT
# --------------------------------------------------

print("\n" + "=" * 60)
print("3. STREAMING + TTFT")
print("=" * 60)

start_time = time.perf_counter()
first_token_time = None
full_response = ""

stream = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Explain AI agents in five short sentences."
        }
    ],
    stream=True
)

for chunk in stream:
    if not chunk.choices:
        continue

    content = chunk.choices[0].delta.content

    if content:
        if first_token_time is None:
            first_token_time = time.perf_counter()

        print(content, end="", flush=True)
        full_response += content

end_time = time.perf_counter()

print()

if first_token_time:
    ttft = first_token_time - start_time
    print("\nTTFT:", round(ttft, 4), "seconds")

total_time = end_time - start_time
print("Total streaming time:", round(total_time, 4), "seconds")


# --------------------------------------------------
# 4. OpenAI-compatible endpoint demonstration
# --------------------------------------------------

print("\n" + "=" * 60)
print("4. OPENAI-COMPATIBLE API")
print("=" * 60)

print("Base URL:")
print("https://api.groq.com/openai/v1")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: API WORKS"
        }
    ]
)

print("Response:", response.choices[0].message.content)