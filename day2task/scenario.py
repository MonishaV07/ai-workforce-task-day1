SCENARIO = """
You are helping organize a college technical event.

The event has a total budget of ₹5,000.

Expenses:
- Venue: ₹1,500
- Certificates: ₹800
- Refreshments: ₹1,200

There are 30 students attending.

Reasoning questions:
1. How much money remains after all three expenses?
2. If the remaining money is divided equally among 30 students,
   how much money can each student receive?

External-information question:
3. What is the current USD to INR exchange rate?

Combined question:
4. If the event gives a $20 prize, what is its approximate value
   in INR using the current USD to INR exchange rate?
"""

BUDGET = 5000
VENUE = 1500
CERTIFICATES = 800
REFRESHMENTS = 1200
STUDENTS = 30
PRIZE_USD = 20