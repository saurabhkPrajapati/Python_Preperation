import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
df1 = df.loc[0:1, :]
df2 = df.loc[2:, :]
df_new = pd.DataFrame({'Name': ['Ram'], 'Age': [67], 'Address': ['unknown'], 'Qualification': ['T.Tech']})
df = pd.concat([df1, df_new, df2], axis=0)
print(df)

# ________________________________________________________________

data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
df.to_csv("/test1.csv")
df.loc[2.5, :] = ['Z', 10, 5, 7]
df = df.sort_index().reset_index(drop=True)
print(df)
