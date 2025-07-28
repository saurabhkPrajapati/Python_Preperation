import pandas as pd

data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)
print(df)
row_index_to_insert = 1
new_row_data = {'A': [8], 'B': [8]}
new_row_data = pd.DataFrame(new_row_data)
part1 = df[:row_index_to_insert]
part2 = df[row_index_to_insert:]

df = pd.concat([part1, new_row_data, part2], axis=0)
df1 = df.reset_index(drop=True).sort_index()
print(df1)

# _____________________________________

data_new = df.copy()  # Create copy of DataFrame
data_new.loc[1.5] = [8, 8]  # Append list at the bottom
data_new = df.sort_index().reset_index(drop=True)  # Reorder DataFrame
print(data_new)
