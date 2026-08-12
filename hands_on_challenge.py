from guided_coding_exercise import load_api_key

def load_config(required_keys: list[str]) -> dict[str, str]:
    # config = {}
    # for key in required_keys:
    #     value = load_api_key(key)
    #     config[key] = value
    return {key: load_api_key(key) for key in required_keys} 

keys = ['OPENAI_API_KEY', 'AZURE_API_KEY', 'DOTNET_API_KEY']
config = load_config(keys)
print(config)