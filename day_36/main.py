import datetime
import json
import os
from pathlib import Path

import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


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


def read_json_as_dict(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


ENV_VALUES = load_env_values(ENV_PATH)
CONFIG_VALUES = read_json_as_dict(CONFIG_PATH)


def get_secret(name, config_key=None):
    env_value = os.getenv(name) or ENV_VALUES.get(name)

    if env_value:
        return env_value

    if config_key:
        config_value = CONFIG_VALUES.get(config_key)

        if config_value:
            return config_value

    raise KeyError(f"Missing required secret: {name}")


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
def getPorcent():
    params = {
        "apikey": get_secret("ALPHAVANTAGE_API_KEY", "stockkey"),
        "function":"TIME_SERIES_DAILY",
        "symbol":STOCK,
    }


    day = datetime.datetime(2025,5,30)
    previus = datetime.datetime(day.year,day.month,day.day-1)


    day = str(day)[:10]
    previus = str(previus)[:10]


    response = requests.get(STOCK_ENDPOINT,params=params).json()


    now = float(response["Time Series (Daily)"][day]["1. open"])
    antes = float(response["Time Series (Daily)"][previus]["4. close"])


    return round(100*antes/now,4)



def getNews():
    params2 = {
        "apiKey": get_secret("NEWS_API_KEY"),
        "q":COMPANY_NAME
    }

    response2 = requests.get(NEWS_ENDPOINT,params=params2).json()

    data = response2.get("articles")[:3]

    print(data[0]["title"])
    print(data[1]["title"])
    print(data[2]["title"])


    





getNews()

if (getPorcent() >= 105):
    getNews()



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

