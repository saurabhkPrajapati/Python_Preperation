import pandas as pd

# Assuming your DataFrame is named 'df'
# Replace df with your actual DataFrame name

# Sample DataFrame creation
data = {'state': ['A', 'A', 'B', 'B', 'C', 'C'],
        'county': ['X', 'Y', 'Z', 'W', 'P', 'Q'],
        'pincode': [1111, 2222, 3333, 4444, 5555, 6666]}
df = pd.DataFrame(data)

# Group by 'state' and find the two largest 'pincode' values for each group
result = df.groupby('state')['pincode'].nlargest(2).tail(-1).reset_index()

# Display the result
print(result)
