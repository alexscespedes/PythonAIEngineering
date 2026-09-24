import threading
from utils.config_helper import load_api_key

class ConfigManager:
     """
     Thread-safe configuration manager for loading and caching environment variables.

     Loads required keys on initialization and caches them in memory.
     Supports reload.
     """
     def __init__(self, required_keys: list[str]):
         self._config: dict[str, str] = {}
         self._lock = threading.Lock()
         self._required_keys = required_keys
         self._load_all_keys(self._required_keys)

     def _load_all_keys(self, keys: list[str]) -> None:
        """Internal helper to load all keys."""
        with self._lock:
             self._config.clear()
             for key in keys:
                 self._config[key] = load_api_key(key)

     def reload(self) -> None:
         """Reload all configuration from environment"""
         self._load_all_keys(self._required_keys)

     def __getitem__(self, key: str) -> str:
         """Allow dict-like access: config['KEY']"""
         with self._lock:
             return self._config[key]

     @property
     def keys(self) -> list[str]:
         """Return list of loaded config keys."""
         with self._lock:
             return list(self._config.keys())
