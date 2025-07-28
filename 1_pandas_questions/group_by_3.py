# importing pandas as pd
import pandas as pd

# sample dataframe
df = pd.DataFrame({'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g',
                         'bar', 'bar', 'foo', 'bar'],
                   'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b']})

# Multi-column frequency count
count = df.groupby(['A']).agg(['count'])
print(count)
count = df.groupby(['A'])['B'].agg(['count'])

# df['A'].value_counts() and df.groupby(['A']).agg(['count']) give same result

size = df.groupby(['A', 'B']).size()
# size is used for when group on multiples columns
print(size)
