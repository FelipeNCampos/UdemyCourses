import requests


MY_LAT = -16.680515
MY_LONG = -49.256127


parameters = {
    "lng" : MY_LONG,
    "lat" : MY_LAT,
}



response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()

print(data)