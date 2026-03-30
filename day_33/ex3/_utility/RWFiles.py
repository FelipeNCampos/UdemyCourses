import json
import os
from pathlib import Path


ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
ENV_KEY_MAP = {
    "smtpPass": "SMTP_PASSWORD",
    "key": "SMTP_PASSWORD",
}


def _load_env_values():
    env_values = {}

    if not ENV_PATH.exists():
        return env_values

    for raw_line in ENV_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        env_values[key.strip()] = value.strip().strip('"').strip("'")

    return env_values


ENV_VALUES = _load_env_values()


class RWFiler():

    @staticmethod
    def getJsonKey(path:str, dictKey):
        env_key = ENV_KEY_MAP.get(dictKey)
        env_value = os.getenv(env_key) if env_key else None

        if env_key and not env_value:
            env_value = ENV_VALUES.get(env_key)

        if env_value:
            return env_value

        try:
            with open(path, "r", encoding="utf-8") as f:
               return json.load(f)[0][dictKey]
        except:
            return "fail read sttpkey"
        
    @staticmethod
    def readJsonToDict(path:str):
        """
        giving path of a json, return a dict of this load json\n
        """
        try:
            with open(path, "r") as f:
                try:
                    return json.load(f)
                except:
                    raise IndexError("erro ao carregar o json")
        except:
            raise IndexError("erro ao abrir o json")
        
        
