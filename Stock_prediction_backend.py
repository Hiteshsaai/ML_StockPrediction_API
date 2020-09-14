# Required Imports

import numpy as np
from urllib.request import urlopen
import json
import ast
import sys
import yfinance as yf
from datetime import datetime
from pandas_datareader import data as pdr
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import pystan
from fbprophet import Prophet


# Creating a stock_data class to return the stock data for which it was searched.
class stock_data:

    def get_jsonparsed_data(self, url):
        """
        Receive the content of ``url``, parse it as JSON and return the object.

        Parameters
        ----------
        url : str

        Returns
        -------
        dict
        """

        response = urlopen(url)
        response = response.read()
        info = response.decode("utf-8")
        info =  ast.literal_eval(info[39:-2])
        result = info['ResultSet']['Result']

        return result




    def get_stockSymbol(self, compName):

        """To get the Stock Symbol/Token Name"""
        compName = compName.strip()
        check_space = compName.split(' ')
        if len(check_space) > 1:
            api_link = f'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={check_space[0]}+{check_space[1]}&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback'

        else:
            api_link = f'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={compName}&region=1&lang=en&callback=YAHOO.Finance.SymbolSuggest.ssCallback'

        result = self.get_jsonparsed_data(api_link)

        if result:
            stock_symbol = result[0]['symbol']
            return stock_symbol
        else:
            return 0




    def get_stock_data(self, compToken, compName):
        # <== that's all it takes :-)
        yf.pdr_override() 

        # download dataframe using pandas_datareader
        stock_price = pdr.get_data_yahoo(compToken, start="2018-01-01", end="2020-08-30")
        
        close_price = stock_price.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], 1)

        return 

        # plt.figure(figsize=(16,8))
        # plt.title(compName.upper(), fontsize = 18)
        # plt.xlabel('Days', fontsize= 18)
        # plt.ylabel('Close Price USD ($)', fontsize = 18)
        # plt.plot(close_price['Close'])
        # plt.show()



# <== that's all it takes :-)
yf.pdr_override() 

# download dataframe using pandas_datareader
stock_price = pdr.get_data_yahoo("GOOGL", start="2018-01-01", end="2020-08-30")

close_price = stock_price.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], 1)


print(close_price['Close'].head())






# Main method to run the code
# if __name__ == "__main__":
#     compName = sys.argv[1]
#     if compName:
#         compTicker = stock_data().get_stockSymbol(compName)
#         print(f'\n {compName} \n')
#         print(stock_data().get_stock_data(compTicker, compName ))

