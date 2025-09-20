from sklearn.neighbors import KNeighborsClassifier

x = [
    [180,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]

y = [0,0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x,y)

weight = float(input("Enter the weight of the Fruit: "))

size = float(input("Enter the size of the Fruit: "))

prediction = model.predict([[weight,size]])[0]

if prediction == 0:
    print("The fruit is Apple.")
else:
    print("The fruit is Orange.")