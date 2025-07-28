import pandas as pd

# list of dicts
input_df = [{'name': 'Sujeet', 'age': 10},
            {'name': 'Sameer', 'age': 11},
            {'name': 'Sumit', 'age': 12}]

df = pd.DataFrame(input_df)
print('Original DataFrame: \n', df)

print('\nRows iterated using iterrows() : ')
for row in df.itertuples():
    # print(row['name'], row['age'])
    print(getattr(row, "name"), getattr(row, "age"))
