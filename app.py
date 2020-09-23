#Importing the required dependencies
from flask import Flask, jsonify, request
from Stock_prediction_backend import stock_data


# Initializing the app
app = Flask(__name__)


# Index endpoint (Explains how to use the url endpoint to get the stock values)
@app.route('/', methods = ['GET'])
def index():
    Intro =  "Welcome to Stock prediction app\nUse the company name and preriod to predict in following order: \n \
    http://127.0.0.1:5000/[COMPANY NAME]/[DURATION]"

    return Intro

 
 # Main url endpoint to get the stock values
@app.route('/<compName>/<int:predict_period>', methods = ['GET'])
def stock_values(compName, predict_period):
    compTicker = stock_data().get_stockSymbol(compName)
    if compTicker:
        return jsonify(stock_data().get_company_prediction(compTicker, predict_period))
    else:
        return "wrong company name"
    
if __name__ == "__main__":
    app.run(debug = True)




