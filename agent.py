"""
System 3: AI Agent

The agent uses:
- an LLM
- tools
- a loop

The LLM decides which tool to use based on the user's question.
"""

import json

from config import client, MODEL, MONTHLY_BUDGET
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = f"""
You are a personal expense AI agent.

You help the user understand their private monthly expense data.

Monthly budget: ₹{MONTHLY_BUDGET}

Available tools:
1. get_expense(category)
   - Retrieves the expense amount for a category from private data.

2. calculator(expression)
   - Performs arithmetic calculations.

Important rules:
- Never guess expense amounts.
- Use get_expense when you need an expense amount.
- Use calculator when arithmetic is required.
- You may use multiple tools if necessary.
- After receiving tool results, continue until you can answer the user's question.
- Give a clear final answer to the user.
"""


def run_agent(question):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    step = 1

    while True:

        print(f"\n--- Agent Step {step} ---")

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0
        )

        message = response.choices[0].message

        # --------------------------------------------------
        # No tool required -> final answer
        # --------------------------------------------------

        if not message.tool_calls:

            print("Agent finished.")

            return message.content.strip()

        # --------------------------------------------------
        # Tool call requested by the LLM
        # --------------------------------------------------

        messages.append(message)

        for tool_call in message.tool_calls:

            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            print(
                f"Tool requested: {tool_name}"
            )

            print(
                f"Arguments: {arguments}"
            )

            # Find the actual Python function
            tool_function = TOOL_FUNCTIONS.get(tool_name)

            if tool_function is None:

                tool_result = f"Unknown tool: {tool_name}"

            else:

                tool_result = tool_function(**arguments)

            print(
                f"Tool result: {tool_result}"
            )

            # Send the tool result back to the LLM
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(tool_result)
                }
            )

        step += 1

        # Safety limit
        if step > 10:
            return "The agent stopped because the maximum number of steps was reached."


# --------------------------------------------------
# Test the AI agent
# --------------------------------------------------

if __name__ == "__main__":

    questions = [

        "How much did I spend on food?",

        "How much did I spend on food and shopping, and what is the total?",

        "How much money will I have left after spending my food and shopping expenses?"

    ]

    print("\n========================================")
    print("       SYSTEM 3: AI AGENT")
    print("========================================")

    for question in questions:

        print("\nQ:", question)

        answer = run_agent(question)

        print("\nFinal Answer:")
        print(answer)

        print("\n" + "=" * 60)