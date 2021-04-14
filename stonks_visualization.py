import pandas_datareader.data as dr
import datetime
import matplotlib.pyplot as plt 
import numpy as np 


#time duration
start = datetime.datetime(2016,1,1)
end = datetime.datetime(2021,1,1)

reliance = dr.DataReader('RELIANCE.NS','yahoo',start,end)
tcs = dr.DataReader('TCS.NS','yahoo',start,end)
infosys = dr.DataReader('INFY.NS','yahoo',start,end)

# reliance.to_csv('Reliance_stock.csv')
# tcs.to_csv('TCS_stock.csv')
# infosys.to_csv('Infosys_stock.csv')

#plot stock price
reliance['Open'].plot(label = 'Reliance',figsize = (15,7))
tcs['Open'].plot(label = 'TCS')
infosys['Open'].plot(label = 'Infosys')
plt.title("Open price comparision")
plt.ylabel('Stock Price')
plt.legend()
plt.show()

#moving average (smooth curve)
reliance['MA50'] = reliance['Open'].rolling(50).mean()
tcs['MA50'] = tcs['Open'].rolling(50).mean()
infosys['MA50'] = infosys['Open'].rolling(50).mean()
reliance['MA50'].plot(label = 'Reliance', figsize = (15,7))
tcs['MA50'].plot(label = 'TCS')
infosys['MA50'].plot(label = 'Infosys')
plt.show()

#volume
reliance['Volume'].plot(label = "Reliance", figsize = (15,7))
tcs['Volume'].plot(label = "TCS")
infosys["Volume"].plot(label = "Infosys")
plt.title("Volume Comparision")
plt.ylabel('Volume')
plt.legend()
plt.show()

#max_volume traded
infosys.iloc[[infosys['Volume'].argmax()]]
tcs.iloc[[tcs['Volume'].argmax()]]
infosys.iloc[370:470]['Open'].plot(figsize = (15,7))
plt.title("SHARP DEEP IN INFOSYS")
plt.show()
tcs.iloc[520:560]['Open'].plot(figsize = (15,7))
plt.title("SHARP DEEP IN TCS")
plt.show()

#total_money_traded
reliance['Total_Money_traded'] = reliance['Open'] * reliance['Volume']
tcs['Total_Money_traded'] = tcs['Open'] * tcs['Volume']
infosys['Total_Money_traded'] = infosys['Open'] * infosys['Volume']

#pllot total_money_traded
reliance['Total_Money_traded'].plot(label = "Reliance", figsize = (15,7))
tcs['Total_Money_traded'].plot(label = "TCS")
infosys["Total_Money_traded"].plot(label = "Infosys")
plt.title("Total_Money_traded Comparision")
plt.ylabel('Total_Money_traded')
plt.legend()
plt.show()

#volatility of stock
reliance['Daily_per_change'] = (reliance['Close']/reliance['Close'].shift(1)) -1
tcs['Daily_per_change'] = (tcs['Close']/tcs['Close'].shift(1)) -1
infosys['Daily_per_change'] = (infosys['Close']/infosys['Close'].shift(1)) -1
reliance.head()

#volatility of stock plot
reliance['Daily_per_change'].plot(label = 'Reliance')
plt.legend()
plt.show()
reliance['Daily_per_change'].plot(label = 'Reliance',kind = 'hist',alpha = 0.5)
tcs['Daily_per_change'].plot(label = 'TCS',kind = 'hist',alpha = 0.5)
infosys['Daily_per_change'].plot(label = 'Infosys',kind = 'hist',alpha = 0.5)
plt.legend()
plt.show()
reliance['Daily_per_change'].plot(label = 'Reliance',kind = 'density')
tcs['Daily_per_change'].plot(label = 'TCS',kind = 'density')
infosys['Daily_per_change'].plot(label = 'Infosys',kind = 'density')
plt.legend()
plt.show()
