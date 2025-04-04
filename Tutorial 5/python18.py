import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("weather.csv")
plt.bar(data["date"], data["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature per Day")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()