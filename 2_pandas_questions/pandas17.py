import pandas as pd
import numpy as np

df = pd.DataFrame({'Geek_ID': ['Geek1_id', 'Geek2_id', 'Geek3_id',
                               'Geek4_id', 'Geek5_id'],
                   'Geek_A': [1, 1, 3, 2, 4],
                   'Geek_B': [1, 2, 3, 4, 6],
                   'Geek_R': np.random.randn(5)})


print(df.Geek_ID.str.split('_').str[0].tolist())
