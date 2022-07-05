#import pandas, matplotlib and datetime etc to work

from cProfile import label
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

from google.colab import files
uploaded = files.upload()

appl = pd.read_csv('AAPL.csv')

plt.figure(figsize=(12.5, 4.5))
plt.plot(AAPL['Adj close price'])
plt.title('Apple Adj. Close Price History')
plt.xlabel('Oct. 02, 2006 - Dec. 30, 2011')
plt.ylabel('Adj. Close price USD ($)')
plt.legend(loc = 'upper left')
plt.show()

SMA30 = pd.DataFrame()
SMA30['Adj Close Price'] = AAPL['Adj CLose Price'].rolling(Windows = 30).mean()

SMA100 = pd.DataFrame()
SMA100['Adj Close Price'] = AAPL['Adj CLose Price'].rolling(Windows = 100).mean()

plt.figure(figsize = (12.5, 4.5))
plt.plot(AAPL['Adj Close Price'], label = 'AAPL')
plt.plot(SMA30['Adj Close Price'], label = 'SMA30')
plt.plot(SMA100['Adj Close Price'], label = 'SMA100')
plt.title('Apple Adj. Close Price History')
plt.xlabel('Oct. 02, 2006 - Dec 30, 2011')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc = 'upper left')
plt.show()

data = pd.DataFrame()
data['AAPL'] = AAPL['Adj Close Price']
data['SMA30'] = SMA30['Adj Close Price']
data['SMA100'] = SMA100['Adj Close Price']

def buy_sell(data):
    sigPriceBuy = []
    sigPricesell = [] 
    flag = -1

    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['AAPL'][i])
                sigPricesell.append(np.man)
                flag = 1
            else:
                sigPriceBuy.append(np.man)
                sigPricesell.append(np.man)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
               sigPriceBuy.append(np.man)
               sigPricesell.append(data['AAPL'][i])
            else:
                sigPriceBuy.append(np.man)
                sigPricesell.append(np.man)
        else:
            













