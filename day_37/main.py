import json
import requests




#util

def readJsonasDict(caminho):
    try:
        with open(caminho, "r") as f :
            return json.loads(f.read())
    except:
        return "Error"




#prog

def do():
    data = readJsonasDict("./.config")
    end = data['end']
    
    params = {
        "token":"#cotoneteste.123",
        "username":"#cotoneteste123",
        "agreeTermsOfService":"yes",
        "notMinor":"yes"
    }



    response = requests.post(end+" /v1/users",params=params)

    print(response)




do()