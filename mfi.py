import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.read_csv('data/output.csv')
data = data.set_index(pd.DatetimeIndex(data['ctmString'].values))

# Period set
period =  14

typical_price = (data['close'] + data['high'] + data['low']) / 3


money_flow = typical_price * data['vol']
money_flow


positive_flow =[] 
negative_flow = [] 


for i in range(1, len(typical_price)):
  if typical_price[i] > typical_price[i-1]: 
    positive_flow.append(money_flow[i-1])
    negative_flow.append(0) 
  elif typical_price[i] < typical_price[i-1]:
    negative_flow.append(money_flow[i-1])
    positive_flow.append(0)
  else: 
    positive_flow.append(0)
    negative_flow.append(0)


positive_mf =[]
negative_mf = [] 


for i in range(period-1, len(positive_flow)):
  positive_mf.append(sum(positive_flow[i+1-period : i+1]))


for i in range(period-1, len(negative_flow)):
  negative_mf.append(sum(negative_flow[i+1-period : i+1]))



mfi = 100 * (np.array(positive_mf) / (np.array(positive_mf)  + np.array(negative_mf) ))

print(mfi)

mfi_data = pd.DataFrame()
mfi_data['MFI'] = mfi


plt.figure(figsize=(12.2,4.5))
plt.plot(data['ctmString'][:123],mfi_data['MFI'], data['ctmString'],data['close'])
plt.axhline(30, linestyle='--', color = 'orange')  
plt.axhline(20, linestyle='--',color = 'blue')  
plt.axhline(80, linestyle='--', color = 'blue') 
plt.axhline(70, linestyle='--', color = 'orange')  
plt.title('MFI')

plt.legend(mfi_data.columns.values, loc='upper left')
plt.show()
