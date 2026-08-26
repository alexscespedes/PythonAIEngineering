# HOW TO RUN FAST API: uvicorn main:app --reload
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from hands_on_challenge import load_config

class ConfigRequest(BaseModel):
    required_keys: list[str]

class ConfigResponse(BaseModel):
    config: dict[str, str]

class AgentResponse(BaseModel):
    message: str
    loaded_count: int

app = FastAPI()

@app.post('/config/load')
async def load_config_async(config_request: ConfigRequest) -> ConfigResponse:
    try:
        config = load_config(config_request.required_keys)
        return ConfigResponse(config=config)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/agent/run')
async def openai_calling_agent(config_request: ConfigRequest) -> AgentResponse:
    """
    Load environment variables for an AI agent.

    Raises:
        - 400 if any required key is missing or empty
    """
    try:
        load_config(config_request.required_keys)
        loaded_count = len(config_request.required_keys)
        return AgentResponse(
            message=f"Loaded {loaded_count} environment variables successfully",
            loaded_count=loaded_count
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
