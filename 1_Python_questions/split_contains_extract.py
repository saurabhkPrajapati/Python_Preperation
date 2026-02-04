import pandas as pd
import numpy as np


df = pd.DataFrame({'Geek_ID': ['Geek1_id', 'Geek2_id', 'Geek3_id',
                               'Geek4_id', 'Geek5_id'],
                   'Geek_A': [1, 1, 3, 2, 4],
                   'Geek_B': [1, 2, 3, 4, 6],
                   'Geek_R': np.random.randn(5)})

print(df.Geek_ID.str.split('_').str[1].tolist())
a = df.Geek_ID.apply(lambda x: x.split('_')[1])
b = df.Geek_ID.str.split('_', expand=True)
list(filter(lambda x: x.__contains__('_'), list(df.Geek_ID)))
print(a)

# ___________________________________________________________________

data = {
    'Text': ['apple123', 'banana456', 'cherry789', 'date101']
}

df = pd.DataFrame(data)

pattern = r'(\d+)'

df['Numbers'] = df['Text'].str.extract(pattern)

print(df)
