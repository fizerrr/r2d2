import numpy as np

def calculate_rsi(prices, period=14):
    print(prices)
    deltas = np.diff(prices)
    print(deltas)
    seed = deltas[:period+1]
    up = seed[seed >= 0].sum()/period
    down = -seed[seed < 0].sum()/period
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:period] = 100. - 100./(1.+rs)
    print(rsi)

    for i in range(period, len(prices)):
        delta = deltas[i-1]  
        if delta > 0:
            upval = delta
            downval = 0.
        else:
           upval = 0.
           downval = -delta

        up = (up*(period-1) + upval)/period
        down = (down*(period-1) + downval)/period
        rs = up/down
        rsi = 100. - 100./(1.+rs)
        print(rsi)
        
    return rsi
