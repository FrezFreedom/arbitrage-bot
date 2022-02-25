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


####################################################

request_to_nobitex = "https://api.nobitex.ir/v2/orderbook/USDTIRT"
    
while True:
    try:
        response_from_nobitex = requests.get(request_to_nobitex)
        nobitex_data = response_from_nobitex.json()
        if nobitex_data['status'] == "ok":
            break
    except Exception as error:
        time.sleep(5)


nobitex_bid_price = nobitex_data['asks'][0][0]
nobitex_ask_price = nobitex_data['bids'][0][0]
nobitex_bid_volume = nobitex_data['asks'][0][1]
nobitex_ask_volume = nobitex_data['bids'][0][1]

print(nobitex_ask_price, nobitex_bid_price, nobitex_ask_volume, nobitex_bid_volume)

#################################################

request_to_exir = "https://api.exir.io/v1/orderbooks?symbol=usdt-irt"
    
while True:
    try:
        response_from_exir = requests.get(request_to_exir)
        break
    except Exception as error:
        time.sleep(5)

exir_data = response_from_exir.json()

raw_exir_data = exir_data['usdt-irt']

exir_bid_price = raw_exir_data['bids'][0][0]
exir_ask_price = raw_exir_data['asks'][0][0]
exir_bid_volume = raw_exir_data['bids'][0][1]
exir_ask_volume = raw_exir_data['asks'][0][1]

print(exir_ask_price, exir_bid_price, exir_ask_volume, exir_bid_volume)

#################################################

request_to_arzpaya = "https://api.arzpaya.com/Public/getorderbook/irt/1"
    
while True:
    try:
        response_from_arzpaya = requests.get(request_to_arzpaya)
        break
    except Exception as error:
        time.sleep(5)

arzpaya_data = response_from_arzpaya.json()

raw_arzpaya_data = arzpaya_data['USDTIR']

arzpaya_bid_price = raw_arzpaya_data['Buys'][0]['Price']
arzpaya_ask_price = raw_arzpaya_data['Sells'][0]['Price']
arzpaya_bid_volume = raw_arzpaya_data['Buys'][0]['Volume']
arzpaya_ask_volume = raw_arzpaya_data['Sells'][0]['Volume']

print(arzpaya_ask_price, arzpaya_bid_price, arzpaya_ask_volume, arzpaya_bid_volume)

#################################################