import cryptocompare as cc
import datetime as dt
import pandas as pd
import csv

currs = ['BTC', 'ETH', 'LTC', 'BCH', 'NEO', 'OMG', 'XRP', 'XMR', 'IOT', 'ZEC', 'DASH']
#cur_list = ','.join(currs)

result = []

for curr in currs:

    result.append(cc.get_price(curr, 'USD'))

prices = []
prices.append((dt.datetime.now()).strftime('%Y-%m-%d %H:%M:%S'))

idx = 0
for data in result:
    prices.append(str(data[currs[idx]]['USD']))
    idx += 1

price_list = ','.join(prices)
price_list = price_list + '\n'

fd = open('price_data.csv', 'a', newline='')
fd.write(price_list)
fd.close()
