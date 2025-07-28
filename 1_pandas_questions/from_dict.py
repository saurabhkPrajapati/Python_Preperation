from collections import OrderedDict

import pandas as pd

# used for following
# dict to dataframe

data = [
        ('Age', [18, 15, 17, 18, 17]),
        ('Team', ['A', 'B', 'A', 'C', 'B']),
        ('Score', [7, 6, 8, 7, 5]),
]

df = pd.DataFrame.from_dict(OrderedDict(data), orient='columns')
print(df)

data = {
        'Age': [18, 15, 17, 18, 17],
        'Team': ['A', 'B', 'A', 'C', 'B'],
        'Score': [7, 6, 8, 7, 5]
        }
df = pd.DataFrame.from_dict(data, orient='index')
print(df)

df = pd.json_normalize(data)
print(df)

data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks': 10, 'For': 20, 'geeks': 30}]
df = pd.json_normalize(data)
print(df)
