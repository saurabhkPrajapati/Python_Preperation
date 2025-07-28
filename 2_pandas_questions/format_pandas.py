import pandas as pd

# create the data dictionary
data = {'Month': ['January', 'February', 'March', 'April'],
        'Expense': [21525220.653, 31125840.875, 23135428.768, 56245263.942]}

# create the dataframe
dataframe = pd.DataFrame(data, columns=['Month', 'Expense'])
dataframe['Expense'] = dataframe['Expense'].astype('float')
print("Given Dataframe :\n", dataframe)
# round to two decimal places in python pandas
# pd.options.display.float_format = '${:,.2f}'.format
dataframe['Expense'] = dataframe.apply(lambda row: '${:,.3f}'.format(row['Expense']), axis=1)  # iterating over
# dataframe = dataframe.applymap(lambda val: '${:,.3f}'.format(val))
dataframe['Expense'] = dataframe['Expense'].apply(lambda x: '${:,.3f}'.format(x))
dataframe['Expense'] = dataframe['Expense'].map(lambda x: '${:,.3f}'.format(x))
print('\nResult :\n', dataframe)
