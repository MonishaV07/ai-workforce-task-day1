from config import ask_llm


def main():

    question = """
A college technical event has a total budget of ₹5,000.

The expenses are:
- Venue: ₹1,500
- Certificates: ₹800
- Refreshments: ₹1,200

There are 30 students attending.

Calculate:
1. The remaining budget.
2. How much of the remaining budget each student would receive
   if it were divided equally among the 30 students.

Give a concise explanation of the calculation and the final answers.
"""

    prompt = f"""
Solve the following problem carefully.

Do the calculations step by step internally, then provide a concise
explanation and the final answer.

Do not use any external tools.

{question}
"""

    print("=" * 60)
    print("CHAIN-OF-THOUGHT / MULTI-STEP REASONING")
    print("=" * 60)

    print("\nQuestion:")
    print(question)

    answer = ask_llm(prompt, temperature=0.2)

    print("\nModel Response:")
    print(answer)


if __name__ == "__main__":
    main()