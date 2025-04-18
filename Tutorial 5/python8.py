import pandas as pd
data = pd.read_csv("stud.csv")
print("All student data:")
print(data)
data.set_index("rollno", inplace=True)
print(data[["name", "mark"]])
print("Sorted by name:")
print(data.sort_values(by="name")[["rollno", "name", "mark"]])
print("Sorted by marks (high to low):")
print(data.sort_values(by="mark", ascending=False)[["rollno", "name", "mark"]])
print("Average marks:", data.mark.mean())
print("Median marks:", data.mark.median())
print("Most common mark:", data.mark.mode()[0])
print("Lowest mark:", data.mark.min())
print("Highest mark:", data.mark.max())
print("Mark variance:", data.mark.var())
print("Mark standard deviation:", data.mark.std())
data.mark.hist()