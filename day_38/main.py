import json
from datetime import datetime
import requests

def teste():
    end = "https://trackapi.nutritionix.com/v2/natural/exercise"



    qst = input("text: ")

    params = {
        "query":qst,
    }

    head = {
        "x-app-id":"6a4a5c3b",
        "x-app-key":"6a1c064a8daada7a27be30168b96f899",
    }

    response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=head)
    data = json.loads(response.text)
    
    with open("log.json", "w") as f:
        json.dump(data, f, indent=4)

    date = datetime.now()
    data_final = date.strftime("%d/%m/%Y")

    horario_final = date.strftime("%H:%M:%S")

    body = {
        "sheet1":{
            "dia": data_final,
            "hora":horario_final,
            "exercicio":data["exercises"][0]["user_input"],
            "tempo":data["exercises"][0]["duration_min"],
            "caloria":data["exercises"][0]["nf_calories"],
        }
    }

    response = requests.post(url="https://api.sheety.co/e2c73a01d895630a39a9f8a79f38600e/workTeste/sheet1",json=body)

teste()
