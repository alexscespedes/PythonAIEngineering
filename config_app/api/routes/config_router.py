from fastapi import APIRouter, HTTPException
from services.config_manager import ConfigManager
from models.config_models import ConfigRequest, ConfigResponse, AgentResponse
from utils.config_helper import load_config

router = APIRouter()

dev_keys = ["OPENAI_API_KEY_DEV", "AZURE_API_KEY_DEV", "DOTNET_API_KEY_DEV"]
config_manager = ConfigManager(dev_keys)

@router.post('/config/load')
async def load_config_async(config_request: ConfigRequest) -> ConfigResponse:
    try:
        config = load_config(config_request.required_keys)
        return ConfigResponse(config=config)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post('/agent/run')
async def openai_calling_agent(config_request: ConfigRequest) -> AgentResponse:
    """
    Load environment variables for an AI agent.

    Raises:
        - 400 if any required key is missing or empty
    """
    try:
        for key in config_request.required_keys:
            _ = config_manager[key]
            

        loaded_count = len(config_request.required_keys)
        return AgentResponse(
            message=f"Loaded {loaded_count} environment variables successfully",
            loaded_count=loaded_count
        )
    except (ValueError, KeyError) as e:
        raise HTTPException(status_code=400, detail=str(e))