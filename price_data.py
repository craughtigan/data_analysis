import cryptocompare as cc
import datetime as dt
import pandas as pd
import time

# get data from csv
df = pd.DataFrame.from_csv('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/price_data.csv')

# list of hours to update for
start = (max(list(df.index))) + dt.timedelta(hours=1)  # hour after last hour in df
end = dt.datetime.now().replace(minute=0, second=0, microsecond=0)  # current hour
times = pd.date_range(start, end, freq='H')

# currency prices to get
currs = ['BTC', 'ETH', 'LTC', 'BCH', 'NEO', 'OMG', 'XRP', 'XMR', 'IOT', 'ZEC', 'DASH']

# open file for new data
fd = open('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/price_data.csv', 'a', newline='')

for t in times:

    # price for each currency
    result = []
    for curr in currs:
        result.append(cc.get_historical_price(curr, 'USD', t))
        # delay for cryptocompare database
        time.sleep(11)

    # create comma delimited string
    prices = []
    prices.append(t.strftime('%Y-%m-%d %H:%M:%S'))

    # append string prices from dicts in order of currency list
    idx = 0
    for data in result:
        prices.append(str(data[currs[idx]]['USD']))
        idx += 1

    prices_string = ','.join(prices)

    # end string with new line
    prices_string = prices_string + '\n'

    # write line to file
    fd.write(prices_string)

# close the file
fd.close()
