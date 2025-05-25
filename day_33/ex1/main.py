import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

data = response.json()


latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude,longitude)
print(iss_position)