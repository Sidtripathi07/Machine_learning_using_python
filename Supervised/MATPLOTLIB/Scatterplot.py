import matplotlib.pyplot as plt

hours = [ 1,2,3,4,5]
scores = [60,75,80,85,90]

plt.scatter(hours,scores, color = 'blue', marker='s', label='Scores' )
plt.title("Study Hours vs Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Scores Obtained")
plt.legend(loc = 'upper left')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.show()