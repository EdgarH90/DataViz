##
# Author: Edgar Hernandez
# Creation Date: 11/30/2019
# Description: This program utilizes the Alhpa Vantage API to retrieve stock price information in JSON format
##

import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

# initialize TimeSeries function with API key
app = TimeSeries('ST5P6JQVLFE5PE5W', output_format= 'pandas')


def getStockData(ticker):
    df = pd.DataFrame()
    for item in ticker:
        stock = app.get_daily(item, outputsize='full')
        # get column with closing price of ticker
        data = pd.DataFrame({f'{item}': stock[0].iloc[:,3]})
        data = data.sort_index()
        data = data.loc['2017-01-01':'2021-02-01']
        print(data.head)
        # add to data frame
        if (df.empty):
            df = df.append(data)
        else:
            df = df.join(data, how = 'outer')
    # save data to .csv file
    df.to_csv('stockData.csv')
    print(df.head())

tickers = ['AMC', 'GME', 'BB', 'PLTR', 'SPCE']

getStockData(tickers)