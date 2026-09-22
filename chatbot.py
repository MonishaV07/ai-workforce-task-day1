"""
System 1: Plain LLM Chatbot

The LLM receives the private expense data and answers
the user's questions. No external tools are used.
"""

from config import client, MODEL, EXPENSE_DATA, MONTHLY_BUDGET


SYSTEM_PROMPT = f"""
You are a personal expense assistant.

You have access to this private monthly financial information:

Monthly Budget: ₹{MONTHLY_BUDGET}

Expenses:
Food: ₹{EXPENSE_DATA["food"]}
Transport: ₹{EXPENSE_DATA["transport"]}
Shopping: ₹{EXPENSE_DATA["shopping"]}
Education: ₹{EXPENSE_DATA["education"]}
Entertainment: ₹{EXPENSE_DATA["entertainment"]}

Answer questions using only the information provided above.
Do not invent expenses or financial information.
"""


def chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    questions = [
        "How much did I spend on food?",
        "How much did I spend on shopping?",
        "What is my monthly budget?",
        "How much did I spend on education?"
    ]

    print("\n=== SYSTEM 1: PLAIN LLM CHATBOT ===\n")

    for question in questions:
        print("Q:", question)
        print("A:", chatbot(question))
        print("-" * 60)