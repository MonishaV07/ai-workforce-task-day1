"""
Tools available to the AI agent.

The agent can:
1. Retrieve an expense from private data.
2. Perform arithmetic calculations.
"""

import ast
import operator

from config import EXPENSE_DATA, MONTHLY_BUDGET


# --------------------------------------------------
# Tool 1: Get expense
# --------------------------------------------------

def get_expense(category: str) -> str:
    """
    Retrieve the expense amount for a category.
    """

    category = category.strip().lower()

    amount = EXPENSE_DATA.get(category)

    if amount is None:
        return f"Unknown expense category: {category}"

    return str(amount)


# --------------------------------------------------
# Tool 2: Calculator
# --------------------------------------------------

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}


def _evaluate(node):

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """
    Evaluate a basic arithmetic expression.
    """

    try:
        result = _evaluate(
            ast.parse(expression, mode="eval").body
        )

        return str(result)

    except Exception as error:
        return f"Calculator error: {error}"


# --------------------------------------------------
# Tool mapping
# --------------------------------------------------

TOOL_FUNCTIONS = {
    "get_expense": get_expense,
    "calculator": calculator
}


# --------------------------------------------------
# Tool schemas given to the LLM
# --------------------------------------------------

TOOLS = [

    {
        "type": "function",
        "function": {
            "name": "get_expense",
            "description": (
                "Get the expense amount for one category "
                "from the private expense data."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": (
                            "Expense category such as food, "
                            "transport, shopping, education, "
                            "or entertainment."
                        )
                    }
                },
                "required": ["category"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Perform arithmetic using numbers, +, -, *, / "
                "and brackets."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression to calculate."
                    }
                },
                "required": ["expression"]
            }
        }
    }

]


# --------------------------------------------------
# Test the tools directly
# --------------------------------------------------

if __name__ == "__main__":

    print("=== TOOL TEST ===")

    print(
        "Food expense:",
        get_expense("food")
    )

    print(
        "Shopping expense:",
        get_expense("shopping")
    )

    print(
        "Total expenses:",
        calculator("4500 + 2000 + 3500 + 5000 + 1500")
    )

    print(
        "Remaining budget:",
        calculator("20000 - 16500")
    )