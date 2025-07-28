import pandas as pd

dict = {'movie_data': ['The Godfather 1972 9.2',
                       'Bird Box 2018 6.8',
                       'Fight Club 1999 8.8']}

# Convert the dictionary to a dataframe
df = pd.DataFrame(dict)

# Extract name from the string
df['Name'] = df['movie_data'].str.extract('(\w*\s[a-zA-Z]*)', expand=True)

# Extract year from the string
df['Year'] = df['movie_data'].str.extract('(\d\d\d\d)', expand=True)

# Extract rating from the string
df['Rating'] = df['movie_data'].str.extract('(\d\.\d)', expand=True)
print(df)
