import pandas as pd

x=pd.read_csv("data.csv")
print(x.tail(3))
print(x.info())
print(x.describe())