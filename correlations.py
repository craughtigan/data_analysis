import pandas as pd
import datetime as dt
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

base_path = '~/Python/PycharmProjects/Crypto/'

mkt_price = pd.read_csv(filepath_or_buffer=base_path + 'market-price.csv'
                         , names=['mkt_price']
                         , parse_dates=True)
difficulty = pd.read_csv(filepath_or_buffer=base_path + 'bitcoin_difficulty.csv'
                         , names=['difficulty']
                         , parse_dates=True)
miner_trans_rev = pd.read_csv(filepath_or_buffer=base_path + 'cost-per-transaction.csv'
                              , names=['trans_rev']
                              , parse_dates=True)
hash_rate = pd.read_csv(filepath_or_buffer=base_path + 'hash-rate.csv'
                        , names=['hash_rate']
                        , parse_dates=True)
trans_per_block = pd.read_csv(filepath_or_buffer=base_path + 'n-transactions-per-block.csv'
                              , names=['block_trans']
                              , parse_dates=True)
unique_addresses = pd.read_csv(filepath_or_buffer=base_path + 'n-unique-addresses.csv'
                               , names=['u_address']
                               , parse_dates=True)
trans_fees = pd.read_csv(filepath_or_buffer=base_path + 'transaction-fees.csv'
                         , names=['trans_fees']
                         , parse_dates=True)

diff_hash = difficulty.join(hash_rate)
count_trans_fees = trans_per_block.join(trans_fees)

all_frames = [difficulty, hash_rate, trans_fees, trans_per_block, miner_trans_rev, unique_addresses]

all_data = mkt_price

for frame in all_frames:
    all_data = all_data.join(frame)


# 50 day rolling averages
difficulty["50_day_avg"] = difficulty.rolling(50, 50).mean()
miner_trans_rev["50_day_avg"] = miner_trans_rev.rolling(50, 50).mean()
hash_rate["50_day_avg"] = hash_rate.rolling(50, 50).mean()
trans_per_block["50_day_avg"] = trans_per_block.rolling(50, 50).mean()
unique_addresses["50_day_avg"] = unique_addresses.rolling(50, 50).mean()
trans_fees["50_day_avg"] = trans_fees.rolling(50, 50).mean()
