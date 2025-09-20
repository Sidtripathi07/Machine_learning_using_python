import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [1000,1200,3000,2000]

plt.plot (x,y,color = 'red', marker ='o', linestyle ='--' ,linewidth = 2 ,markersize = 5)
plt.title("Sales over the years")
plt.xlabel("Years")
plt.ylabel("Sales in USD")
plt.legend(["Sales"],loc = 'upper left')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.xlim (1,6)
plt.ylim(0,6000)
plt.xticks([1,2,3,4],['M1','M2','M3','M4'])
plt.show()