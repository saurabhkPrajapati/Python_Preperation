import pandas as pd

data = {'text_column': ["Hello text World", "Python text Programming", "Data text Analysis"]}
df = pd.DataFrame(data)

# Split at "text" and remove the ending part
split_value = "text"
# split operation on whole column( column is series)
df['text_column'] = df['text_column'].str.split(split_value).str[0]

# Print the modified DataFrame
print(df)
