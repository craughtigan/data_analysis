import cryptocompare as cc
import time
import pandas as pd

result = []

times = pd.date_range('01/01/2017', '09/30/2017', freq='H')

fd = open('/Users/cameronraughtigan/Python/PycharmProjects/data_analysis/btc.csv', 'a', newline='')

for t in times:

    result = cc.get_historical_price('BTC', 'USD', t)
    row = t.strftime('%Y-%m-%d %H:%M:%S') + ',' + str(result['BTC']['USD'])
    fd.write(row)
    time.sleep(11)

fd.close()


