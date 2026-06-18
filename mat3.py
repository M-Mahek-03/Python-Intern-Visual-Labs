import csv
import matplotlib.pyplot as mlp
import pandas as pd 

data = [
    ["Name", "Age", "Gender"],
    ["John", 30, "Male"],
    ["Jane", 25, "Female"],
    ["Bob", 40, "Male"],
]

with open("data2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    

df = pd.read_csv("data2.csv")

mlp.plot(df["Age"], df["Weight"])
mlp.xlabel("Age")
mlp.ylabel("Weight")
mlp.title("Age vs. Weight")
mlp.show()
