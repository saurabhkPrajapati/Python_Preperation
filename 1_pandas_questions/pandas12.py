import pandas as pd

# Create the dataframe
df = pd.DataFrame({'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11', '12/23/1234'],
                   'Event': ['Music', 'Poetry', 'Theatre', 'Comedy', 'nan'],
                   'Cost': [10000, 5000, 15000, 2000, 60000]})

# Print the dataframe
print(df)
lis = []
for index, row in df.iterrows():
    lis.append([row['Date'], row['Event'], row['Cost']])

print(lis)

Row_list = []
for i in range((df.shape[0])):
    Row_list.append(list(df.iloc[i, :]))

print(Row_list)



