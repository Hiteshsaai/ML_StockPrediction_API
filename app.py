#Importing the required dependencies
from flask import Flask, jsonify, request
from main import stock_data


# Initializing the app 
app = Flask(__name__)


# Index endpoint (Explains how to use the url endpoint to get the stock values)
@app.route('/', methods = ['GET'])
def index():
    Intro =  "Welcome to Stock prediction app\nUse the company name and preriod to predict in following order: \n \
    https://stockprediction-ml.herokuapp.com/[COMPANY NAME]/[DURATION] \n NOTE: if Company has two names you can use space in the url endpoint (Eg:General Motors)"

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


