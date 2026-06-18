import pandas as pd 

x = pd.read_csv("data1.csv")
print(x)

print(x["Age"])
print(x["Age"].describe())