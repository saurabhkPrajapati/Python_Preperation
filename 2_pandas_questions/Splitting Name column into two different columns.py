import pandas as pd

df = pd.DataFrame({'Name': ['John_Larter', 'Robert_Junior', 'Jonny_Depp'],
                   'Age': [32, 34, 36]})

print("Given Dataframe is :\n", df)

print("\nSplitting Name column into two different columns :")
# df[['First', 'Last']] = df['Name'].str.split(expand=True)
# df1 = pd.DataFrame(df['Name'].str.split().tolist(), columns=['first', 'Last'])

df[['First', 'Last']] = df.Name.apply(lambda x: pd.Series(x.split("_")))
print(df)
