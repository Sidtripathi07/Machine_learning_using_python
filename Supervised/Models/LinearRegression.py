from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]
Y = [40, 50, 65, 75, 90]

model = LogisticRegression()

model.fit(X,Y)

hours = float(input("Enter the number of hours you studied: "))
predicted_score = model.predict([[hours]])

print(f"Predicted score for studying {hours} hours: {predicted_score}")