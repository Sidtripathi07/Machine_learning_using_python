import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd

data = pd.read_csv('/Users/siddharthtripathi/Downloads/Pandas/students.csv')

X = data[['Hours']]
Y = data ['Score']

model = LinearRegression()

model.fit(X,Y)

Predicted_score = model.predict(X)

MAE = mean_absolute_error(Y, Predicted_score)
MSE = mean_squared_error(Y, Predicted_score)
RMSE = np.sqrt(MSE)

print(f"Mean Absolute Error: {MAE}")
print(f"Mean Squared Error: {MSE}")
print(f"Root Mean Squared Error: {RMSE}")

new_prediction = model.predict([[7]])
print(f"Prediction for 7 hours of study is score = {new_prediction}")

new_hour = float(input("Enter the number of Hours = "))
new_pred = model.predict(pd.DataFrame([[new_hour]], columns =['Hours']))
print(f"Prediction for {new_hour} is score = {new_pred}")

new_prediction = model.predict([[7]])
print(f"Prediction for 7 hours of study is score = {new_prediction}")