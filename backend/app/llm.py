import os
from groq import Groq
from dotenv import load_dotenv

# Compute absolute path → backend/.env
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path)

MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

def generate_sql_from_nl(nl_query: str) -> str:
    API_KEY = os.getenv("GROQ_API_KEY")
    client = Groq(api_key=API_KEY)

    resp = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": (
                "You are an expert SQL generator for SQLite.\n\n"
                "DATABASE SCHEMA:\n"
                "TABLE customers(\n"
                "  customer_id INTEGER,\n"
                "  name TEXT,\n"
                "  gender TEXT,\n"
                "  location TEXT\n"
                ")\n\n"
                "STRICT RULES:\n"
                "1. Only use columns from the schema: customer_id, name, gender, location.\n"
                "2. If the user mentions 'city', 'place', 'area', 'town', or 'from <x>',\n"
                "   ALWAYS map it to the column 'location'.\n\n"
                "3. ALL text comparisons must be case-insensitive using:\n"
                "      LOWER(column) = LOWER('value')\n"
                "4. Only generate a single SELECT query, no explanations.\n"
                "5. Use COUNT(), DISTINCT, GROUP BY when user asks for them.\n"
                "6. Never hallucinate columns or use dangerous SQL.\n"
            )
        },
        {"role": "user", "content": nl_query}
    ],
    max_tokens=200
)


    return resp.choices[0].message.content.strip()
