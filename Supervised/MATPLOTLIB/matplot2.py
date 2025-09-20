import matplotlib.pyplot as plt

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
y = [8, 5, 7, 8 ,2]

plt.plot(x,y)

plt.title("Bakery sales this week")
plt.xlabel("Day of the weeks")
plt.ylabel("Sales in a Day")

plt.show()