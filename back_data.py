import cryptocompare as cc
import time
import pandas as pd
import datetime as dt

df = pd.DataFrame.from_csv('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/market-price.csv')

start = (max(list(df.index))) + dt.timedelta(days=1)
end = dt.datetime.now().replace(minute=0, second=0, microsecond=0)

times = pd.date_range(start, end, freq='D')

for t in times:

    result = cc.get_historical_price('BTC', 'USD', t)
    row = t.strftime('%Y-%m-%d %H:%M:%S') + ',' + str(result['BTC']['USD']) + '\n'
    fd = open('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/market-price.csv', 'a', newline='')
    fd.write(row)
    fd.close()
    time.sleep(10)
