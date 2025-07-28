import pandas as pd

df = pd.DataFrame({"Name": ['Tom', 'Nick', 'John', 'Peter'],
                   "Age": [15, 26, 17, 28]}, index=["a", "b", "c", "d"])

print(df)
# df = df.rename({"a": "e", "b": "f", "c": "g", "d": "h"}, axis=0)
df.rename({"Name": "e", "Age": "f"}, axis=1, inplace=True)
print(df)

