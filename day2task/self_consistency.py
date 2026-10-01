from collections import Counter
from config import ask_llm


QUESTION = """
A college technical event has a budget of ₹5,000.

The expenses are:
- Venue: ₹1,500
- Certificates: ₹800
- Refreshments: ₹1,200

There are 30 students.

What is the remaining budget, and how much would each student
receive if the remaining amount were divided equally?
"""


def run_experiment(temperature, runs):

    answers = []

    print("=" * 60)
    print(f"TEMPERATURE = {temperature}")
    print("=" * 60)

    for i in range(runs):

        prompt = f"""
Solve this reasoning problem carefully.

{QUESTION}

Provide the final numerical answers with a concise explanation.
"""

        answer = ask_llm(prompt, temperature=temperature)

        answers.append(answer)

        print(f"\n--- Run {i + 1} ---")
        print(answer)

    return answers


def extract_final_answer(text):

    """
    A simple normalization function for comparing responses.

    The complete response is retained for inspection.
    """

    return " ".join(text.lower().split())


def main():

    # ---------------------------------------------------------
    # NON-ZERO TEMPERATURE
    # ---------------------------------------------------------

    answers = run_experiment(
        temperature=0.8,
        runs=5
    )

    normalized = [
        extract_final_answer(answer)
        for answer in answers
    ]

    counts = Counter(normalized)

    print("\n" + "=" * 60)
    print("SELF-CONSISTENCY OBSERVATION")
    print("=" * 60)

    print("\nNumber of runs:", len(answers))

    print("\nMost frequent complete response:")
    print(counts.most_common(1)[0])

    # ---------------------------------------------------------
    # TEMPERATURE ZERO
    # ---------------------------------------------------------

    print("\n\n")
    print("=" * 60)
    print("TEMPERATURE = 0")
    print("=" * 60)

    zero_answers = run_experiment(
        temperature=0,
        runs=3
    )

    print("\nTemperature 0 responses were generated for comparison.")


if __name__ == "__main__":
    main()