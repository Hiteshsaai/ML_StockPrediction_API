# Importing the required libraries
import numpy as np 
from urllib.request import urlopen
import json
import ast
import sys
import yfinance as yf
# from pandas_datareader import data as pdr
from datetime import datetime
from fbprophet import Prophet
import json

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

        """To get the Stock Symbol/Token Name 
        we are using the YahooFinance API"""

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



    def get_company_prediction(self, comp_ticker, num_days_to_predict):

        """
        Getting the stock data from yfinance and using it 
        to predicted the outputs by using 
        fb prophet library and storing the date, inputdata and predicted data in a json formate 
        """

        
        result = {}

        # Generating Today's date for the uptodate record
        curr_date = datetime.today().strftime('%Y-%m-%d')

        # download dataframe using pandas_datareader
        # data = pdr.get_data_yahoo(comp_ticker, start="2019-01-01", end= curr_d1)
        data = yf.download(comp_ticker, start="2018-01-01", end=curr_date,)

        # Selecting only the closing price for the model
        close_price = data[['Close']]

        # Making date as a column from index
        date_index = list(close_price.index)
        
        close_price.insert(1,'Date', date_index, True)


        # Rename the features: These names are NEEDED for the model fitting
        close_price = close_price.rename(columns = {"Date":"ds","Close":"y"}) #renaming the columns of the dataset

        # Fitting the prophet model
        m = Prophet(daily_seasonality = True) # the Prophet class (model)
        m.fit(close_price) # fit the model using all data

        future = m.make_future_dataframe(periods= num_days_to_predict) #we need to specify the number of days in future
        prediction = m.predict(future)
        
        date = list(prediction['ds'])
        
        #Converting the date from timestamp to string formate
        
        date_in_str = []
        for d in date:
            d = str(d).split(' ')[0]
            
            date_in_str.append(d)

        stock_data = list(close_price['y'])

        pred_data = list(prediction['yhat'].iloc[-num_days_to_predict:])

        result['Company_Ticker'] = comp_ticker
        
        result['date'] =  date_in_str
        
        result['stock_values'] = stock_data
        
        result['stock_pred_values'] = pred_data

        return result



# Main method to run the code
if __name__ == "__main__":

    compName = "microsoft"
    days_to_predict = 90

    if compName and days_to_predict:
        compTicker = stock_data().get_stockSymbol(compName)
        if compTicker:
            print(stock_data().get_company_prediction(compTicker, days_to_predict))
        else:
            print("wrong company name")

    else:
        print("Missing Argument: Result cannot be producted")

