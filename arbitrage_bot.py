from itertools import cycle
from api_keys import *
import time
import requests


bomb = u'\U0001F4A3'
nazar = u'\U0001F9FF'
check_mark = u'\U00002705'

def send_message_to_arbitrage_channel(message_):
    try:
        requests.get('https://api.telegram.org/bot5175422403:AAEQkqkYYGQCS84WIXevC-ed2ruZZGKQHhU/sendMessage?chat_id=-1001543655927&text=' + message_ +'&parse_mode=html')
    except Exception as error:
        print("Telegram api has some problems, in line 21 error is: " + str(error))
        print("bot will go sleep for 5 seconds!")
        time.sleep(5)


while True:
    all_crypto_shop = []
    request_to_wallex = "https://api.wallex.ir/v1/depth?symbol=USDTTMN"
        
    while True:
        try:
            response_from_wallex = requests.get(request_to_wallex)
            break
        except Exception as error:
            time.sleep(5)

    wallex_data = response_from_wallex.json()

    raw_wallex_data = wallex_data['result']

    wallex_bid_price = float(raw_wallex_data['bid'][0]['price'])
    wallex_ask_price = float(raw_wallex_data['ask'][0]['price'])
    wallex_bid_volume = float(raw_wallex_data['bid'][0]['quantity'])
    wallex_ask_volume = float(raw_wallex_data['ask'][0]['quantity'])

    print("wallex ", wallex_ask_price, wallex_bid_price, wallex_ask_volume, wallex_bid_volume)

    all_crypto_shop.append(("wallex", wallex_ask_price, wallex_bid_price, wallex_ask_volume, wallex_bid_volume))

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


    nobitex_bid_price = float(nobitex_data['asks'][0][0]) / 10.00
    nobitex_ask_price = float(nobitex_data['bids'][0][0]) / 10.00
    nobitex_bid_volume = float(nobitex_data['asks'][0][1])
    nobitex_ask_volume = float(nobitex_data['bids'][0][1])

    print("nobitex ", nobitex_ask_price, nobitex_bid_price, nobitex_ask_volume, nobitex_bid_volume)

    all_crypto_shop.append(("nobitex", nobitex_ask_price, nobitex_bid_price, nobitex_ask_volume, nobitex_bid_volume))

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

    exir_bid_price = float(raw_exir_data['bids'][0][0])
    exir_ask_price = float(raw_exir_data['asks'][0][0])
    exir_bid_volume = float(raw_exir_data['bids'][0][1])
    exir_ask_volume = float(raw_exir_data['asks'][0][1])

    print("exir ", exir_ask_price, exir_bid_price, exir_ask_volume, exir_bid_volume)

    all_crypto_shop.append(("exir", exir_ask_price, exir_bid_price, exir_ask_volume, exir_bid_volume))

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

    arzpaya_bid_price = float(raw_arzpaya_data['Buys'][0]['Price'])
    arzpaya_ask_price = float(raw_arzpaya_data['Sells'][0]['Price'])
    arzpaya_bid_volume = float(raw_arzpaya_data['Buys'][0]['Volume'])
    arzpaya_ask_volume = float(raw_arzpaya_data['Sells'][0]['Volume'])

    print("arzpaya ", arzpaya_ask_price, arzpaya_bid_price, arzpaya_ask_volume, arzpaya_bid_volume)

    all_crypto_shop.append(("arzpaya", arzpaya_ask_price, arzpaya_bid_price, arzpaya_ask_volume, arzpaya_bid_volume))

    #################################################

    request_to_okex = "https://ok-ex.io/server/api/order/order-books"
        
    while True:
        try:
            response_from_okex = requests.get(request_to_okex)
            break
        except Exception as error:
            time.sleep(5)

    okex_data = response_from_okex.json()

    for crypto in okex_data:
        if crypto['market']['symbol']=="USDTIRT":
            okex_bid_price = float(crypto['bids'][len(crypto['bids'])-1]['p'])
            okex_ask_price = float(crypto['asks'][0]['p'])
            okex_bid_volume = float(crypto['bids'][len(crypto['bids'])-1]['qt'])
            okex_ask_volume = float(crypto['asks'][0]['qt'])
            break


    print("okex ", okex_ask_price, okex_bid_price, okex_ask_volume, okex_bid_volume)

    all_crypto_shop.append(("okex", okex_ask_price, okex_bid_price, okex_ask_volume, okex_bid_volume))

    #################################################

    for shop_a in all_crypto_shop:
        for shop_b in all_crypto_shop:
            if shop_a[2]/shop_b[1] >= 1.008:
                send_message_to_arbitrage_channel( check_mark + " " + shop_a[0] + " ----> " + shop_b[0] + " " + str(shop_a[2]/shop_b[1]) +  " \n")
                message_send = ""
                for shop in all_crypto_shop:
                    message_send += nazar + " " + str(shop[0]) + " ap: " + str(shop[1]) + " bp: " + str(shop[2]) + " av: " + str(shop[3]) + " bv: " + str(shop[4]) + "\n------------------------------------------------------\n"    
                send_message_to_arbitrage_channel(message_send)
    
    time.sleep(35)