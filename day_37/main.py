import json
import os
from pathlib import Path
import requests
from datetime import datetime 



#util

ENV_PATH = Path(__file__).with_name(".env")
CONFIG_PATH = Path(__file__).with_name(".config")


def load_env_values(path):
    env_values = {}

    if not path.exists():
        return env_values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        env_values[key.strip()] = value.strip().strip('"').strip("'")

    return env_values


def readJsonasDict(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f :
            return json.loads(f.read())
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


ENV_VALUES = load_env_values(ENV_PATH)
CONFIG_VALUES = readJsonasDict(CONFIG_PATH)


def get_setting(name, default=None, config_key=None):
    env_value = os.getenv(name) or ENV_VALUES.get(name)

    if env_value:
        return env_value

    if config_key:
        config_value = CONFIG_VALUES.get(config_key)

        if config_value:
            return config_value

    if default is not None:
        return default

    raise KeyError(f"Missing required setting: {name}")




#prog

def createUser(user):
    end = get_setting("PIXELA_ENDPOINT", "https://pixe.la", "end")
    
    params = {
        "token": get_setting("PIXELA_TOKEN"),
        "username": user,
        "agreeTermsOfService":"yes",
        "notMinor":"yes"
    }



    response = requests.post(end+"/v1/users",json=params)

    print(response.json())


def createGraph(user):
    end = get_setting("PIXELA_ENDPOINT", "https://pixe.la", "end")


    config = {
        "id":"codegraph",
        "name":"Code Graph",
        "unit":"commit",
        "type":"int",
        "color":"sora"
    }

    headers = {
        "X-USER-TOKEN": get_setting("PIXELA_TOKEN")
    }


    response = requests.post(url=f"{end}/v1/users/{user}/graphs",json=config, headers=headers)
    print(response)

def getGraph(user,id):
    end = get_setting("PIXELA_ENDPOINT", "https://pixe.la", "end")
    target = end+f"/v1/users/{user}/graphs/{id}"

    response = requests.get(target)

    with open("./result.svg", "w") as f:
        f.write(response.text)

def addPixel(user, iden, amont:str):
    end = get_setting("PIXELA_ENDPOINT", "https://pixe.la", "end")
    target = end+f"/v1/users/{user}/graphs/{iden}"

    date = datetime.now()
    teste = date.strftime("%Y%m%d")

    params = {
        "date":str(teste),
        "quantity":str(amont),
    }

    headers = {
        "X-USER-TOKEN": get_setting("PIXELA_TOKEN")
    }

    response = requests.post(url=target, json=params, headers=headers)
    print(response)




addPixel("cotonete1","codegraph",5)
