import cryptocompare as cc
import datetime as dt
import pandas as pd

pull_time = dt.datetime.now().replace(minute=0, second=0, microsecond=0)

df = pd.DataFrame.from_csv('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/price_data.csv')

start = (max(list(df.index))) + dt.timedelta(hours=1)
end = dt.datetime.now().replace(minute=0, second=0, microsecond=0)

times = pd.date_range(start, end, freq='H')

currs = ['BTC', 'ETH', 'LTC', 'BCH', 'NEO', 'OMG', 'XRP', 'XMR', 'IOT', 'ZEC', 'DASH']

result = []

fd = open('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/price_data.csv', 'a', newline='')

for t in times:
    for curr in currs:
        result.append(cc.get_historical_price(curr, 'USD', t))
    
    prices = []
    prices.append(t.strftime('%Y-%m-%d %H:%M:%S'))

    idx = 0
    for data in result:
        prices.append(str(data[currs[idx]]['USD']))
        idx += 1

    price_list = ','.join(prices)
    price_list = price_list + '\n'
    fd.write(price_list)

fd.close()
