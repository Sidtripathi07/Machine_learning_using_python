import matplotlib.pyplot as plt

revenue = [5000, 7000, 8000, 6000]
products = ['IDLI', 'SAMBAR', 'CHUTNEY', 'DOSA']

plt.pie (revenue, labels=products, autopct= '%1.1f%%', startangle=140)
plt.title("Product-wise Revenue Distribution")
plt.show()