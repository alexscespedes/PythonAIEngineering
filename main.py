# HOW TO RUN FAST API: uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from hands_on_challenge import load_config

class ConfigRequest(BaseModel):
    required_keys: list[str]

class ConfigResponse(BaseModel):
    config: dict[str, str]

app = FastAPI()

@app.post('/config/load')
async def load_config_async(config_request: ConfigRequest) -> ConfigResponse:
    try:
        config = load_config(config_request.required_keys)
        return ConfigResponse(config=config)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))