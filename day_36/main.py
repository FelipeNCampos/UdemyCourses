import requests
import json
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


#util

c
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
def getPorcent():
    params = {
        "apikey":readJsonasDict("./.config")["stockkey"],
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
        "apiKey":"696b27f058ca4f0fbd4b439c60bc3729",
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

