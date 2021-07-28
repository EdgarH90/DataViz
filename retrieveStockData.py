##
# Author: Edgar Hernandez
# Creation Date: 11/30/2019
# Description: This program utilizes the Alhpa Vantage API to retrieve stock price information in JSON format
##

import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies

# initialize TimeSeries function with API key
app = TimeSeries('ST5P6JQVLFE5PE5W', output_format= 'pandas')
cryptoApp = CryptoCurrencies('ST5P6JQVLFE5PE5W', output_format= 'pandas')

def getAssetData(ticker, isEquity = True):
    df = pd.DataFrame()
    if isEquity:
        for item in ticker:
            stock = app.get_daily(item, outputsize='full')
            # get column with closing price of ticker
            data = pd.DataFrame({f'{item}': stock[0].iloc[:,3]})
            data = data.sort_index()
            data = data.loc['2017-01-01':'2021-07-01']
            print(data.head)
            # add to data frame
            if (df.empty):
                df = df.append(data)
            else:
                df = df.join(data, how = 'outer')
        df.to_csv('stockData.csv')
    else:
        for item in ticker:
            coin = cryptoApp.get_digital_currency_daily(item, market='USD')
            # get column with closing price of ticker
            data = pd.DataFrame({f'{item}': coin[0].iloc[:,3]})
            data = data.sort_index()
            data = data.loc['2017-01-01':'2021-07-01']
            print(data.head)
            # add to data frame
            if (df.empty):
                df = df.append(data)
            else:
                df = df.join(data, how = 'outer')
        df.to_csv('cryptoData.csv') 
    # save data to .csv file
    print(df.head())

cryptos = ['ADA', 'DOGE', 'XRP']

#getAssetData(cryptos, False)

#tickers = ['AMC', 'GME', 'BB', 'PLTR', 'SPCE']
#getAssetData(tickers)

df = pd.read_csv('stockData.csv')

print(df.head())
stacked = df.melt(id_vars=['date'], var_name = "Asset" , value_name = "Value")
print("Melted: \n")
print(stacked[0:10])
stacked.to_csv('stockData.csv')
