from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]
Y = [0,0,1,1,1]

model=LogisticRegression()
model.fit(X,Y)

hours = float(input("Enter the number of hours you studied: "))

predicted_class = model.predict([[hours]])[0]

if predicted_class == 1:
    print("The model predicts you will pass.")
else:
    print('The model predicts you will Fail.')
