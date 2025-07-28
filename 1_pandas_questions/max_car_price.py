import pandas as pd

df = pd.read_csv(r'C:\Users\91880\PycharmProjects\pythonProject\Automobile_data.csv')
car_Manufacturers = df.groupby('company')
priceDf = car_Manufacturers['price'].max()
priceDf
