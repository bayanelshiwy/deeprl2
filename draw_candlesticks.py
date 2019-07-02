import sys
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates


if __name__ == "__main__":
    file_to_open = sys.argv[1]  # 0 is the index of name of python prog, 1 is the index of first argument in command line.
    data = pd.read_csv(file_to_open, sep=',')

    data['<DATE>'] = pd.to_datetime(data['<DATE>'])
    data["<DATE>"] = data["<DATE>"].apply(mdates.date2num)

    ohlc = data[['<DATE>', '<OPEN>', '<HIGH>', '<LOW>', '<CLOSE>']].copy()

    f1, ax = plt.subplots(figsize=(15, 8))
    candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    # Saving image
    plt.savefig('candlestick.png')