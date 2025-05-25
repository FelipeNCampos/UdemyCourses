import requests
from datetime import datetime
from smtp.doSMTP import DoSMTP
from _utility.RWFiles import RWFiler
MY_LAT = -16.680515
MY_LONG = -49.256127



def getIss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")

    data = response.json()


    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    iss_position = (latitude,longitude)
    return iss_position

def daySunTime():

    parameters = {
        "lng" : MY_LONG,
        "lat" : MY_LAT,
        "formatted":0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    day = (sunrise,sunset,time_now)
    return day


def challenge():

    intervalo = 5

    alcanceX = [MY_LONG-intervalo,MY_LONG+intervalo]
    alcanceY = [MY_LAT-intervalo,MY_LAT+intervalo]

    
    iss_position = getIss_position()
    
    sun = daySunTime()

    if iss_position[0] in alcanceY and iss_position[1] in alcanceX:
        if sun[2]>=sun[0] and sun[2]<=sun[1]:
            print("Look up, u can see")
            key = RWFiler.getJsonKey("config.json","smtpPass")
            do = DoSMTP("felipe.n.cmp@gmail.com","smtp.google.com",key)
            do.sendMessage("felipe.n.cmp@gmail.com","ISS está visivel no ceu","A estação espacial ISS deve estar visivel no ceu nesse momento")
    else:
        print("Be pacient")


challenge()
    



