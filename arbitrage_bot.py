from api_keys import *
import time
import requests

request_to_wallex = "https://api.wallex.ir/v1/markets"
    
while True:
    try:
        response_from_wallex = requests.get(request_to_wallex)
        break
    except Exception as error:
        time.sleep(5)

wallex_data = response_from_wallex.json()

raw_wallex_data = wallex_data['result']['symbols']['USDTTMN']['stats']

wallex_bid_price = raw_wallex_data['bidPrice']
wallex_ask_price = raw_wallex_data['askPrice']
wallex_bid_volume = raw_wallex_data['bidVolume']
wallex_ask_volume = raw_wallex_data['askVolume']

print(wallex_ask_price, wallex_bid_price, wallex_ask_volume, wallex_bid_volume)