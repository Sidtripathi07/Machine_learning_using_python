import matplotlib.pyplot as plt

scores = [55, 78, 45, 89, 66, 92, 73, 84, 91, 77, 68, 80, 76,89 ,94 ,72, 88, 95, 67, 81]

plt.hist(scores, bins=[40, 50, 60, 70, 80, 90, 100], color='purple', edgecolor='black')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.title("Distribution of Student Scores")
plt.xlabel("Score Ranges")
plt.ylabel("Number of Students")
plt.show()