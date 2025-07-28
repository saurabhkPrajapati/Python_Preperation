import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['a', 'b', 'c', 'd', 'e'],
    'C': [1.1, '1.0', '1.3', 2, 5]})

convert_dict = {'A': int,
                'C': float
                }
# df = df.astype(str)
df = df.astype(convert_dict)
print(df.dtypes)
