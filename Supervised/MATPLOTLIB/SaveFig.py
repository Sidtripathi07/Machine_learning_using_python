import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [12, 8, 5, 7, 11]

plt.plot(x, y, color='blue')
plt.title("Line Plot")
plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')
plt.show()

