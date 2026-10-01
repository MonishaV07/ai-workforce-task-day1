from config import ask_llm
from tools import get_exchange_rate, calculate_prize_inr


def main():

    question = """
The college technical event wants to give a $20 prize.

What is the approximate value of this prize in INR using the
current USD to INR exchange rate?

You must use the exchange-rate tool to obtain the current rate.
"""

    print("=" * 60)
    print("REACT AGENT")
    print("=" * 60)

    print("\nQuestion:")
    print(question)

    # ---------------------------------------------------------
    # THOUGHT
    # ---------------------------------------------------------

    print("\nThought:")
    print("I need the current USD to INR exchange rate.")

    # ---------------------------------------------------------
    # ACTION
    # ---------------------------------------------------------

    print("\nAction:")
    print("get_exchange_rate()")

    try:
        result = get_exchange_rate()

        # -----------------------------------------------------
        # OBSERVATION
        # -----------------------------------------------------

        print("\nObservation:")
        print(result)

        rate = result["rate"]

        # -----------------------------------------------------
        # SECOND THOUGHT
        # -----------------------------------------------------

        print("\nThought:")
        print(
            f"I obtained the current USD to INR rate "
            f"({rate:.2f}). I can now convert the $20 prize."
        )

        # -----------------------------------------------------
        # ACTION
        # -----------------------------------------------------

        print("\nAction:")
        print("calculate_prize_inr(20, exchange_rate)")

        prize_inr = calculate_prize_inr(20, rate)

        # -----------------------------------------------------
        # OBSERVATION
        # -----------------------------------------------------

        print("\nObservation:")
        print(f"$20 × ₹{rate:.2f} = ₹{prize_inr:.2f}")

        # -----------------------------------------------------
        # FINAL ANSWER
        # -----------------------------------------------------

        final_prompt = f"""
Answer the user's question using the following tool observation.

Current USD to INR exchange rate:
₹{rate:.2f} per USD

The $20 prize is approximately:
₹{prize_inr:.2f}

Give a concise final answer and mention that the exchange rate
came from the external exchange-rate tool.
"""

        final_answer = ask_llm(final_prompt, temperature=0)

        print("\nFinal Answer:")
        print(final_answer)

    except Exception as e:
        print("\nTool Error:")
        print(e)


if __name__ == "__main__":
    main()