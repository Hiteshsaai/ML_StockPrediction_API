<img src="stock_prediction.png" align="center" />

# ML StockPrediction API

## About

It is a REST API which predicts the future stock values of company. This API return a JSON file which contains,
- **Company Name** 
- **Stock price Date** *(From 2018/01/01 - Current Date)
- **Predicted Stock values** *(Based on Mentioned duration)*
- **Exisiting Stock values** 

## Technique Used

We have use ARIM (Auto regression Intergrated Moving Avreage) & Prophet model methods to predict the stock values with normalization. 


## How to use?

Use the following link below  </br>

https://ml-stockprediction-hitesh.herokuapp.com/

To get the stock predicted values for different companies, you have to mention the company-name and prediction duration. </br>

Take a look at some Examples,

<ins> Example1 </ins>
- ```https://stockprediction-ml.herokuapp.com/tesla/100``` </br>
  - This link will tempt to return stock predictions for **TESLA** for the next **100** working days.
  
<ins> Example2 </ins>
- If the company name has two names or space between names mention the company name with space itself or else api wont be able to recognize, like below,
  ```diff
  + Do this: https://ml-stockprediction-hitesh.herokuapp.com/general motors/365
  - Not this: https://ml-stockprediction-hitesh.herokuapp.com/generalmotors/365
  ```

  - The above example link will tempt to return stock predictions for **General Motors** for the next **365** working days.



