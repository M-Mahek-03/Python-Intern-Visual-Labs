import csv
import matplotlib.pyplot as plt
import pandas as pd

# Create a list of data
data = [
    ["Name", "Age", "Weight"],
    ["John", 30, "31.0"],
    ["Jane", 25, "45.8"],
    ["Bob", 40, "33.9"],
]

# Create a CSV file writer
with open("data2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv("data.csv")

# Plot the data
plt.plot(df["Age"], df["Weight"])
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs. Weight")
plt.show()