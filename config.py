import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVIDER = os.getenv("PROVIDER", "groq")
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "qwen/qwen3.8-27b")

if not API_KEY:
    raise SystemExit("GROQ_API_KEY not found. Check your .env file.")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=API_KEY
)

# Private expense data for this project
EXPENSE_DATA = {
    "food": 4500,
    "transport": 2000,
    "shopping": 3500,
    "education": 5000,
    "entertainment": 1500
}

MONTHLY_BUDGET = 20000