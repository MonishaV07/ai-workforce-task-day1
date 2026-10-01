from config import ask_llm
from scenario import SCENARIO


def main():

    question = """
The college technical event has a budget of ₹5,000.

Venue costs ₹1,500.
Certificates cost ₹800.
Refreshments cost ₹1,200.

How much money remains after all expenses?
"""

    prompt = f"""
You are a college event planning assistant.

Answer the question directly and briefly.

{question}
"""

    print("=" * 60)
    print("DIRECT PROMPTING")
    print("=" * 60)

    print("\nQuestion:")
    print(question)

    answer = ask_llm(prompt, temperature=0)

    print("\nFinal Answer:")
    print(answer)


if __name__ == "__main__":
    main()