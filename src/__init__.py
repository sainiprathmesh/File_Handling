import calendar
import json
import time
import requests

ts = time.time()


def get_bitcoin_price():
    URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,INR"  # REPLACE WITH CORRECT URL
    response = requests.request("GET", URL)
    response = json.loads(response.text)
    current_price = response["INR"]
    return current_price


f = open("log.txt", "w+")

while True:
    print(get_bitcoin_price(), time.ctime(calendar.timegm(time.gmtime())))
    f.write(get_bitcoin_price())
    time.sleep(1)
