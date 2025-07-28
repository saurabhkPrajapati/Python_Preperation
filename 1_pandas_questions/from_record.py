import pandas as pd
# used for following
# list of lists,
# list of tuples,
# list of dict,
# list of DataFrame

data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
 {'Geeks': 10, 'For': 20, 'geeks': 30}]

data = [('Peter', 18, 7),
        ('Riff', 15, 6),
        ('John', 17, 8),
        ('Michel', 18, 7),
        ('Sheli', 17, 5)]

data = [['Peter', 18, 7],
        ['Riff', 15, 6],
        ['John', 17, 8],
        ['Michel', 18, 7],
        ['Sheli', 17, 5]]

df = pd.DataFrame.from_records(data)

print(df)
