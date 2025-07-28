import pandas as pd

# Initialise data to lists.
data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks': 10, 'For': 20}]  # not passing 'geeks' value


df = pd.DataFrame(data, index=['1', '2'])
print(df)
