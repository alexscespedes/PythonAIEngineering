import os
from dotenv import load_dotenv

load_dotenv()

def load_api_key(env_var: str) -> str:
    value = os.getenv(env_var, "").strip()
    if not value:
        raise ValueError(f"Environment variable '{env_var}' is missing or empty!")
    return value

def load_config(required_keys: list[str]) -> dict[str, str]:
    return {key: load_api_key(key) for key in required_keys} 