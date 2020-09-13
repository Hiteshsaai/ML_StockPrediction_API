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
            return "Incorrect company name"




    def get_stock_data(self, compToken):
        # <== that's all it takes :-)
        yf.pdr_override() 

        # download dataframe using pandas_datareader
        data = pdr.get_data_yahoo(compToken, start="2020-01-01", end="2020-08-30")
        

# <== that's all it takes :-)
yf.pdr_override() 

# download dataframe using pandas_datareader
stock_price = pdr.get_data_yahoo("TSLA", start="2020-01-01", end="2020-08-30")



plt.figure(figsize=(16,8))
plt.title('Tesla', fontsize = 18)
plt.xlabel('Days', fontsize= 18)
plt.ylabel('Close Price USD ($)', fontsize = 18)
plt.plot(stock_price['Close'])
plt.show()



# # Main method to run the code
# if __name__ == "__main__":
#     print(stock_data().get_stockSymbol("facebook"))
