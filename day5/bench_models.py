from openai import OpenAI
import os
import time
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODELS = [
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b"
]

PROMPTS = [
    "Reply with exactly: OK",
    "In two sentences, what is an AI agent?",
    "A student has a scholarship of 50000 rupees and spends 65 percent of it. How much money remains?"
]


def benchmark(model, prompt):
    start = time.perf_counter()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    end = time.perf_counter()

    elapsed = end - start
    answer = response.choices[0].message.content

    completion_tokens = 0

    if response.usage:
        completion_tokens = response.usage.completion_tokens

    if elapsed > 0:
        tokens_per_second = completion_tokens / elapsed
    else:
        tokens_per_second = 0

    return answer, elapsed, completion_tokens, tokens_per_second


print("=" * 70)
print("GROQ MODEL BENCHMARK")
print("=" * 70)

for prompt_number, prompt in enumerate(PROMPTS, start=1):

    print("\n" + "-" * 70)
    print("PROMPT", prompt_number)
    print("-" * 70)
    print(prompt)

    for model in MODELS:

        print("\nModel:", model)

        try:
            answer, elapsed, tokens, speed = benchmark(
                model,
                prompt
            )

            print("Response:", answer)
            print("Time:", round(elapsed, 4), "seconds")
            print("Completion tokens:", tokens)
            print("Approx. tokens/sec:", round(speed, 2))

        except Exception as e:
            print("ERROR:", e)