import pandas as pd
from coinbase.wallet.client import Client
from decimal import Decimal
from blockchain import statistics

# connection to Coinbase
# client = Client(,)

# minimum currency amount accepted
currs = client.get_currencies()
min_currencies = pd.DataFrame.from_records(currs.data)

cryptos = ('BTC', 'ETH', 'LTC')

# cryptos_df_list = []
cryptos_df = pd.DataFrame()

for crypto in cryptos:
    ex_rates = client.get_exchange_rates(currency=crypto)
    df = pd.DataFrame.from_dict(ex_rates.rates, orient='index').reset_index()
    df = df.rename(columns={'index': 'Currency', 0: 'Rate/' + crypto})
    cryptos_df = pd.concat([cryptos_df, df], axis=1)

# remove duplicate columns (T is transpose)
cryptos_df = cryptos_df.T.drop_duplicates().T

cryptos_df.to_csv(path_or_buf='~/Python/PycharmProjects/Crypto/rates.csv')

spot_price = client.get_spot_price(currency_pair='ETH-USD')
buy_price = client.get_buy_price(currency_pair='ETH-USD')
sell_price = client.get_sell_price(currency_pair='ETH-USD')
price_spread = float(Decimal(sell_price['amount']) - Decimal(buy_price['amount']))

stats = statistics.get()
