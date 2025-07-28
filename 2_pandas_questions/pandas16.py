import pandas as pd

df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
                   'Cost': [10000, 5000, 15000, 2000]})

print(df)

df['Discounted_Price'] = df.Cost.map(lambda x: x - x*.1)
df['Discounted_Price'] = df.Cost.apply(lambda x: x - x*.1)
