import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


symbol = "AAPL"


def get_sma(prices, rate):
    return prices.rolling(rate).mean()

def get_bollinger_bands(prices, rate=20):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()

    bollinger_up = sma + std * 3 # Calculate top band
    bollinger_down = sma - std * 3 # Calculate bottom band

    return bollinger_up, bollinger_down

symbol = 'AAPL'
df = pd.read_csv('AAPL_1min_last_5_years.csv')
df.index = np.arange(df.shape[0])
closing_prices = df['Close']

bollinger_up, bollinger_down = get_bollinger_bands(closing_prices)


# plt.title(symbol + ' Bollinger Bands')
# plt.xlabel('Days')
# plt.ylabel('Closing Prices')
# plt.plot(closing_prices, label='Closing Prices')
# plt.plot(bollinger_up, label='Bollinger Up', c='g')
# plt.plot(bollinger_down, label='Bollinger Down', c='r')
# plt.legend()
# plt.show()