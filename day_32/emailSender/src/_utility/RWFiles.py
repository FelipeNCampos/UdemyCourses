import json
import os
from pathlib import Path


ENV_PATH = Path(__file__).resolve().parents[2] / ".env"


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


class RWFiiler():

    @staticmethod
    def getSTTPkey():
        env_value = os.getenv("SMTP_PASSWORD") or ENV_VALUES.get("SMTP_PASSWORD")

        if env_value:
            return env_value

        try:
            with open("key.json", "r", encoding="utf-8") as f:
               return json.load(f)[0]['key']
        except:
            return "fail read sttpkey"
