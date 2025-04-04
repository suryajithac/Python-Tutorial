import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("sales.csv")
plt.scatter(data["month_number"], data["toothpaste"])
plt.title("Toothpaste Sales per Month")
plt.xlabel("Month")
plt.ylabel("Toothpaste Sales")
plt.show()
data[["facecream", "facewash"]].plot(kind="bar")
plt.title("Facecream and Facewash Sales")
plt.show()
data[["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]].sum().plot(kind="pie", autopct='%1.1f%%')
plt.title("Product Sales Share")
plt.show()