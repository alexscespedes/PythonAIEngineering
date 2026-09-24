from pydantic import BaseModel

class ConfigRequest(BaseModel):
    required_keys: list[str]

class ConfigResponse(BaseModel):
    config: dict[str, str]

class AgentResponse(BaseModel):
    message: str
    loaded_count: int