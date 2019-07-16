import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from pandas_datareader import data, wb
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates


if __name__ == "__main__":
    file_to_open = sys.argv[1]  # 0 is the index of name of python prog, 1 is the index of first argument in command line.
    data = pd.read_csv(file_to_open, sep=',')
    ma = "ma"
    macd = "macd"
    # data["MA50"] = data['<OPEN>'].rolling(20).mean()
    # ema12 = data['<CLOSE>'].ewm(span=12,min_periods=12,adjust=False).mean()
    # ema26 = data['<CLOSE>'].ewm(span=26,min_periods=26,adjust=False).mean()
    # data["MACD"] = ema12 - ema26
    # print(data.head(30))
    arg = sys.argv[2]
    if arg == ma:
        data['<DATE>'] = pd.to_datetime(data['<DATE>'])
        data["<DATE>"] = data["<DATE>"].apply(mdates.date2num)
        data["MA50"] = data['<OPEN>'].rolling(20).mean()
        sma = data["MA50"]
        ohlc = data[['<DATE>', '<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>']].copy()
        f1, ax = plt.subplots(figsize=(15, 8))
        candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
        ax.plot(data['<DATE>'], sma, label='SMA')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        plt.savefig('sma_arguments_ma.png')
        data.to_csv('sma_arguments_ma.csv', index=False)
    elif arg == macd:
        data['<DATE>'] = pd.to_datetime(data['<DATE>'])
        data["<DATE>"] = data["<DATE>"].apply(mdates.date2num)
        ema12 = data['<CLOSE>'].ewm(span=12, min_periods=12, adjust=False).mean()
        ema26 = data['<CLOSE>'].ewm(span=26, min_periods=26, adjust=False).mean()
        data["MACD"] = ema12 - ema26
        ohlc = data[['<DATE>', '<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>']].copy()
        f1, ax = plt.subplots(figsize=(15, 8))
        candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
        ax.plot(data['<DATE>'], data["MACD"], label='MACD')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        plt.savefig('sma_arguments_macd.png')
        data.to_csv('sma_arguments_macd.csv', index=False)