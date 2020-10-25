import json
import calendar

import pandas
import requests
import time
import simplejson


'''def get_bitcoin_price():
    URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR,INR"  # REPLACE WITH CORRECT URL
    response = requests.request("GET", URL)
    response = simplejson.loads(response.text)
    current_price = response["INR"]
    return current_price


ts = time.time()
f = open("log.txt", "w+")

while True:
    print(get_bitcoin_price(), time.ctime(calendar.timegm(time.gmtime())))
    f.write(str(get_bitcoin_price())+" "+time.ctime(calendar.timegm(time.gmtime()))+"\n")
    time.sleep(1)'''
'''def btc():
    URL = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=INR&limit=1800"
    response = requests.request("GET", URL)
    response = simplejson.loads(response.text)
    #current_price = response["INR"]
    #return current_price
    return response


print(btc())'''
k = pandas.read_csv("inr.csv")
