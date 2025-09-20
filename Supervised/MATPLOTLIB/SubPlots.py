import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [12, 8, 5, 7, 11]

plt.subplot(1, 2, 2)
plt.plot(x, y, color='blue')
plt.title("Line Plot")

plt.subplot(1, 2, 1)
plt.bar(x, y, color='orange')
plt.title("Bar Chart")

plt.tight_layout()
plt.show()  