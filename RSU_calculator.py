import requests
from bs4 import BeautifulSoup
import time


STOCKS = 200
TAXBRACKET = 0.35
STARTPRICE = 21
STOCKSIMBOL = 'MBLY'
COIN = 'ILS'

while True:
    stock_value_reader = requests.get(f'https://www.google.com/finance/quote/{STOCKSIMBOL}:NASDAQ')
    conversion_value_reader= requests.get(f'https://www.google.com/finance/quote/USD-{COIN}')
    stock_parsser = BeautifulSoup(stock_value_reader.content, "html.parser")
    coin_parsser = BeautifulSoup(conversion_value_reader.content, "html.parser")
    stock_value = stock_parsser.find("div", {"class":"YMlKec fxKbKc"})
    conversion_value = coin_parsser.find("div", {"class":"YMlKec fxKbKc"})
    print(f'The current Value is: {stock_value.text.strip()} for 1 stock and {conversion_value.text.strip()} {COIN} for 1$  --->   1 stock {float(stock_value.text.strip()[1:])*float(conversion_value.text.strip())} {COIN}')
    price = float(stock_value.text.strip()[1:])
    USD2NIS = float(conversion_value.text.strip())
    sell = STOCKS * price * USD2NIS
    now = sell - sell * 0.12 - TAXBRACKET*sell
    twoY = sell - 0.12*STARTPRICE - (STARTPRICE*STOCKS*USD2NIS)*TAXBRACKET - (price-STARTPRICE)*STOCKS*USD2NIS * 0.25
    print(f'for {STOCKS} stocks you get {round(now,2)} {COIN} if you sell now')
    print(f'for {STOCKS} stocks you get {round(twoY,2)} {COIN} if you sell in 2 years')
    print(f"If you wait two years you will profit {round(twoY-now,2)} {COIN}")
    print("=========================================================================================")
    time.sleep(30)
