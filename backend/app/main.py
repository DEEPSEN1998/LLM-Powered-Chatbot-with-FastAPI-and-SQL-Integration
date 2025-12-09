from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .llm import generate_sql_from_nl
from .db import execute_sql
import os

app = FastAPI()

# Load API token
API_TOKEN = os.getenv("API_TOKEN")

# --- ADD CORS HERE ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # or ["http://localhost:5173"] for stricter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------

class QueryIn(BaseModel):
    query: str

@app.post("/query")
def query_endpoint(payload: QueryIn, authorization: str = Header(None)):

    # simple token-based check (optional)
    if API_TOKEN:
        if not authorization or authorization != f"Bearer {API_TOKEN}":
            raise HTTPException(status_code=401, detail="Unauthorized")

    nl = payload.query
    print("NL Query:", nl)

    # LLM → SQL Conversion
    try:
        sql = generate_sql_from_nl(nl)
        print("Generated SQL:", sql)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM call failed: {e}")

    # Only allow SELECT (safety)
    if not sql.strip().lower().startswith("select"):
        raise HTTPException(status_code=400, detail="Only SELECT queries are allowed")

    # Execute SQL
    try:
        results = execute_sql(sql)
        return {"query": nl, "sql": sql, "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SQL execution error: {e}")
