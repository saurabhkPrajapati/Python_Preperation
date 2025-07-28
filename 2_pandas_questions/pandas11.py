import pandas as pd

# Let's create the dataframe
df = pd.DataFrame({'Date': ['10/2/2011', '12/2/2011', '13/2/2011', '14/2/2011'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
                   'Cost': [10000, 5000, 15000, 2000]})

# Let's visualize the dataframe
print(df)

new_df = pd.DataFrame([['10/2/2023', 'Wrestling', 10000]], columns=['Date', 'Event', 'Cost'])
temp = pd.concat([df.iloc[:2], new_df, df.iloc[2:]])
print(temp)
