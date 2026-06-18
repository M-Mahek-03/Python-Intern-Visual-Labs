import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('music.csv')

# Display the first few rows of the DataFrame
print("First few rows:")
print(df.head())

# Display the last few rows of the DataFrame
print("Last few rows:")
print(df.tail())

# Display basic information about the DataFrame
print("DataFrame info:")
print(df.info())

# Display summary statistics of the DataFrame
print("DataFrame description:")
print(df.describe())

# Provided data
data = {
    'age': [27, 30, 31, 34, 35],
    'gender': [1, 1, 1, 1, 1],
    'genre': ['Accoustic', 'Classical', 'Classical', 'Classical', 'Classical']
}

# Convert provided data into DataFrame
additional_df = pd.DataFrame(data)

# Append additional data to the original DataFrame
df = df._append(additional_df, ignore_index=True)

# Display the updated DataFrame
print("Updated DataFrame:")
print(df)