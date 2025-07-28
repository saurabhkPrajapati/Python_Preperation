import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\saurabh\PycharmProjects\alamgir\Automobile_data.csv")
filter = df['price'] == df['price'].max()
df.loc[filter]

