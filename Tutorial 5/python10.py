import matplotlib.pyplot as plt
months = [1, 2, 3]
sales1 = [200, 400, 100]
sales2 = [300, 600, 200]
plt.plot(months, sales1, label="Product A")
plt.plot(months, sales2, label="Product B")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Comparison")
plt.legend()
plt.show()