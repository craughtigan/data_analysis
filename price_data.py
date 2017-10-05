import cryptocompare as cc
import datetime as dt

currs = ['BTC', 'ETH', 'LTC', 'BCH', 'NEO', 'OMG', 'XRP', 'XMR', 'IOT', 'ZEC', 'DASH']
#cur_list = ','.join(currs)

result = []

pull_time = dt.datetime.now().replace(minute=0, second=0, microsecond=0)

for curr in currs:

    result.append(cc.get_historical_price(curr, 'USD', pull_time))

prices = []
prices.append(pull_time.strftime('%Y-%m-%d %H:%M:%S'))

idx = 0
for data in result:
    prices.append(str(data[currs[idx]]['USD']))
    idx += 1

price_list = ','.join(prices)
price_list = price_list + '\n'

fd = open('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/price_data.csv', 'a', newline='')
fd.write(price_list)
fd.close()
