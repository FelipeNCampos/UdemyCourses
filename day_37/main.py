import json
import requests
from datetime import datetime 



#util

def readJsonasDict(caminho):
    try:
        with open(caminho, "r") as f :
            return json.loads(f.read())
    except:
        return "Error"




#prog

def createUser(user):
    data = readJsonasDict("./.config")
    end = data['end']
    
    params = {
        "token":"##cotoneteste123",
        "username": user,
        "agreeTermsOfService":"yes",
        "notMinor":"yes"
    }



    response = requests.post(end+"/v1/users",json=params)

    print(response.json())


def createGraph(user):
    data = readJsonasDict("./.config")
    end = data["end"]


    config = {
        "id":"codegraph",
        "name":"Code Graph",
        "unit":"commit",
        "type":"int",
        "color":"sora"
    }

    headers = {
        "X-USER-TOKEN":"##cotoneteste123"
    }


    response = requests.post(url=f"https://pixe.la/v1/users/{user}/graphs",json=config, headers=headers)
    print(response)

def getGraph(user,id):
    data = readJsonasDict("./.config")
    end = data['end']
    target = end+f"/v1/users/{user}/graphs/{id}"

    response = requests.get(target)

    with open("./result.svg", "w") as f:
        f.write(response.text)

def addPixel(user, iden, amont:str):
    data = readJsonasDict("./.config")
    end = data['end']
    target = end+f"/v1/users/{user}/graphs/{iden}"

    date = datetime.now()
    teste = date.strftime("%Y%m%d")

    params = {
        "date":str(teste),
        "quantity":str(amont),
    }

    headers = {
        "X-USER-TOKEN":"##cotoneteste123"
    }

    response = requests.post(url=target, json=params, headers=headers)
    print(response)




addPixel("cotonete1","codegraph",5)