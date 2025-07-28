import pandas as pd

# Sample DataFrame
data = {'Expense': [1000.12345, 2000.23456, 3000.34567],
        'Revenue': [4000.45678, 5000.56789, 6000.67890]}
df = pd.DataFrame(data)

# Row to insert
new_row = pd.DataFrame({'Expense': [1500.12345], 'Revenue': [4500.45678]})

# Index where you want to insert the new row
index = 1

# Split the DataFrame at the desired index
upper_part = df.iloc[:index]
lower_part = df.iloc[index:]

# Concatenate the upper part, new row, and lower part
df = pd.concat([upper_part, new_row, lower_part]).reset_index(drop=True)

print(df)
