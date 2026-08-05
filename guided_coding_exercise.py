import os
from dotenv import load_dotenv

load_dotenv()

# key = os.getenv("API_KEY")

def load_api_key(env_var: str) -> str:
    value = os.getenv(env_var, "").strip()
    if not value:
        raise ValueError(f"Environment variable '{env_var}' is missing or empty!")
    return value
    

env = load_api_key("OPENAI_API_KEY")
print(env)