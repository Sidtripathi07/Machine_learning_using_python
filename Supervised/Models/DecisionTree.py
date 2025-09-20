from sklearn.tree import DecisionTreeClassifier

X =[
    [7,2],
    [8,3],
    [9,8],
    [10,9]
]

Y = [0,0,1,1]

model = DecisionTreeClassifier()

model.fit(X,Y)

size = float(input("Enter the size of the Fruit: "))
shade =  float(input("Enter the shade of the Fruit (1-10): "))

result = model.predict([[size,shade]])[1]

if result == 0: 
    print("The fruit is Apple.") 
else:
    print("The fruit is Orange.") 

