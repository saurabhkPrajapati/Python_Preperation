import pandas as pd

df = pd.DataFrame({'City': ['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'],
                   'Cost': [10000, 5000, 15000, 2000, 12000]})

index_ = [pd.Period('02-02-2018'), pd.Period('02-04-2018'),
          pd.Period('02-06-2018'), pd.Period('02-10-2018'), pd.Period('02-12-2018')]

df.index = index_

print(df)
df_updated = df.replace(to_replace='[nN]ew', value='New_', regex=True)

# Print the updated dataframe
print(df_updated)
