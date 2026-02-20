import os
from dotenv import load_dotenv
from pathlib import Path

# --- SENIOR ENGINEER FIX ---
# Instead of just load_dotenv(), we calculate the path.
# This file is in: src/core/config.py
# .parent = src/core
# .parent.parent = src
# .parent.parent.parent = PROJECT_ROOT (where .env is)
env_path = Path(__file__).resolve().parent.parent.parent / '.env'

print(f"DEBUG: Loading .env from: {env_path}") # Debug print to see what's happening
load_dotenv(dotenv_path=env_path)
# ---------------------------

class Config:
    GROQ_API_KEY= os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    MODEL_NAME = "llama-3.1-8b-instant"

    @classmethod
    def validate(cls):
        # Debugging prints to help us see exactly what Python sees
        if not cls.GROQ_API_KEY:
            print("ERROR: GROQ_API_KEY is None. Check .env content.")
        if not cls.TAVILY_API_KEY:
            print("ERROR: TAVILY_API_KEY is None. Check .env content.")

        if not cls.GROQ_API_KEY:
            raise ValueError("Missing GROQ_API_KEY in .env file")
        if not cls.TAVILY_API_KEY:
            raise ValueError("Missing TAVILY_API_KEY in .env file")

Config.validate()