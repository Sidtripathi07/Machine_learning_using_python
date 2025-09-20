import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022]
sales = [2500, 3000, 4000, 3500, 5000]

plt.barh( years,sales, color='blue',label='Sales')
plt.title("Annual Sales")
plt.xlabel("Years")
plt.ylabel("Sales in USD")
plt.legend()
plt.show()