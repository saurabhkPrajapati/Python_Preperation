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
grouped = df.groupby(['Category', 'Subcategory']).agg(['sum', 'mean', 'max', 'min', 'count'])
print(grouped)
# __________________________________________________________
technologies = ({
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark", "Python", "NA"],
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000, 22000, 1500],
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '30days', '50days', '40days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, None, 1400, 1600, 0]
})
df = pd.DataFrame(technologies)
print(df)
# df2 = df.groupby(by=['Courses'], dropna=False).aggregate({'Fee': 'sum', 'Discount': ['sum', 'max']})
df2 = df.groupby(by=['Courses', 'Duration'], dropna=False)
df2.get_group(('Python', '40days'))
print(df2)
