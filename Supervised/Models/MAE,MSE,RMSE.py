from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

real_scores = [90, 60, 85, 95, 70]
predicted_scores = [80, 65, 80, 85, 90]

mea = mean_absolute_error(real_scores,predicted_scores)
mse = mean_squared_error(real_scores,predicted_scores)
rmse = np.sqrt(mse)

print(f'Mean Absolute Error: {mea}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')