def get_sma(prices, rate):
    return prices.rolling(rate).mean()

def get_bollinger_bands(prices, rate=20,error = 1.8):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()

    bollinger_up = sma + std *  error
    bollinger_down = sma - std *  error

    return bollinger_up, bollinger_down
