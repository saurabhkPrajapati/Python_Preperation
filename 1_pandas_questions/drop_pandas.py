import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}

df = pd.DataFrame(data)

df.drop(df.columns[[0, 4, 2]], axis=1, inplace=True, )
# df.drop(df.iloc[:, 1:3], inplace=True, axis=1)
# df.drop(['A', 'B'], axis=1)
# df.drop([0, 1], axis=0)
# print(df)
