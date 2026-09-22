"""
System 2: Rule-Based Workflow

This system uses predefined rules and program logic.
It does NOT use an LLM.
"""

from config import EXPENSE_DATA, MONTHLY_BUDGET


def total_expenses():
    return sum(EXPENSE_DATA.values())


def remaining_budget():
    return MONTHLY_BUDGET - total_expenses()


def budget_status():
    total = total_expenses()

    if total <= MONTHLY_BUDGET:
        return "Within budget"
    else:
        return "Over budget"


def expense_category(category):
    category = category.lower().strip()

    if category in EXPENSE_DATA:
        return EXPENSE_DATA[category]
    else:
        return None


def workflow(question):
    """
    Handle predefined questions using fixed rules.
    """

    question = question.lower()

    # Rule 1: Ask for a specific category
    for category in EXPENSE_DATA:
        if category in question:
            amount = expense_category(category)
            return f"You spent ₹{amount} on {category}."

    # Rule 2: Ask for total expenses
    if "total" in question or "spent" in question and "how much" in question:
        return f"Your total expenses are ₹{total_expenses()}."

    # Rule 3: Ask for remaining budget
    if "remaining" in question or "left" in question:
        return f"You have ₹{remaining_budget()} remaining from your monthly budget."

    # Rule 4: Ask whether the budget is exceeded
    if "within budget" in question or "over budget" in question:
        return f"Your budget status is: {budget_status()}."

    # If no predefined rule matches
    return "Sorry, I cannot handle this question because no predefined rule matches it."


if __name__ == "__main__":

    questions = [
        "How much did I spend on food?",
        "How much did I spend on shopping?",
        "What are my total expenses?",
        "How much money do I have left?",
        "Am I within budget?",
        "Can you give me advice about reducing my entertainment expenses?"
    ]

    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW ===\n")

    for question in questions:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 60)