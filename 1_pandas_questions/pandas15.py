import pandas as pd

df = pd.DataFrame({'Date': ['11/8/2011', '11/9/2011', '11/10/2011',
                            '11/11/2011', '11/12/2011'],
                   'Event': ['Music', 'Poetry', 'Music', 'Comedy', 'Poetry']})

print(df)


def set_value(row_number, assigned_value):
    return assigned_value[row_number]


event_dictionary = {'Music': 1500, 'Poetry': 800, 'Comedy': 1200}

df['Price'] = df['Event'].apply(lambda x: event_dictionary[x], event_dictionary)
# df['Price'] = df['Event'].apply(lambda x: event_dictionary[x])
# df['Price'] = df['Event'].map(lambda x: event_dictionary[x])

print(df)
