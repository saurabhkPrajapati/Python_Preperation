import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcategory': ['X', 'X', 'X', 'Y', 'X'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Grouping by 'Category' and 'Subcategory' columns and calculating the sum for each group
grouped = df.groupby(['Category', 'Subcategory']).sum()
print(grouped)
# ________________________________________________________
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Grouping by 'Category' and 'Subcategory' columns and calculating multiple aggregation functions
grouped = df.groupby(['Category', 'Subcategory']).agg(['sum', 'mean', 'max', 'min'])
print(grouped)
