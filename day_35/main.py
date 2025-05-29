from _util.RW import RW
import requests

rw = RW()
MY_LAT = -16.680515
MY_LONG = -49.256127

print(rw.getKey("key"))

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid": rw.getKey("key")
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall",params=parameters)
print(response)