import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('AAPL_1min_last_5_years.csv')
data = data.set_index(pd.DatetimeIndex(data['Date'].values))

n = 20
max  = 2519
dif =  0


x=data['Date'][:max]
y=data['Close'][:max]

average = []

def moving_average():
    for i in range(max):
        avg = 0
        if i>=n:
            for j in range(n):
                avg = avg + data['Close'][i-j]
                # print(data['Close'][j])
            avg = avg / n
            average.append(avg)
        else:
            average.append(0)

moving_average()

average_1 = []
average_2 = []

for i in average:
    average_1.append(i + dif)
    average_2.append(i - dif)

plt.plot(x,y,x,average_1,x,average_2)
plt.show()