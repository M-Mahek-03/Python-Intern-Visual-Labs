import pandas as pd

# Create a DataFrame with the correct syntax
y = pd.DataFrame({"name": ["Iqra", "Mehrin", "Mahek", "Aamina"]}, index=["A", "B", "C", "D"])

# Print the DataFrame
print(y)

# Update names in the DataFrame
y["name"] = ["Sauleha", "Alfina", "Nureen", "Zoya"]
print(y)

# Add a new column "name1" to the DataFrame
y["name1"] = ["Sauleha", "Alfina", "Nureen", "Zoya"]
print(y)

# Assuming you want to add an "age" column, add it like this:
y["age"] = [20, 22, 21, 19]

# Print summary statistics for the "age" column
print(y["age"].describe())

# Update the age for the first row
y.at["A", "age"] = 21  # Correct way to modify the value in a DataFrame
print(y)
