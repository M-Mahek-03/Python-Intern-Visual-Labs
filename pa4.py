#Create a excel file and read panda
import pandas as pd

x=pd.read_excel("data.excel")
print(x.tail(3))
print(x.info())
print(x.describe())