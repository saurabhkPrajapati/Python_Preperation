# importing pandas as pd
import pandas as pd

# sample dataframe
df = pd.DataFrame({'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g',
                         'bar', 'bar', 'foo', 'bar'],
                   'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b']})

# Multi-column frequency count
count = df.groupby(['A']).count()
print(count)

size = df.groupby(['A', 'B']).size()
print(size)
