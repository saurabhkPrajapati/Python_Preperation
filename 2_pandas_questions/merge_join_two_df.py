import pandas as pd

Car_Price = pd.DataFrame(
    {'Company': ['Toyota', 'Honda', 'BMV', 'Audi', 'Royce'], 'Price': [23845, 17995, 135925, 71400, 90000]},
    index=['a', 'b', 'c', 'd', 'e'])
car_Horsepower = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]},
                              index=['a', 'b', 'c', 'd'])

# Merge DataFrames based on the 'ID' column
result_df = pd.merge(Car_Price, car_Horsepower, on='Company', how='inner')

pd.concat([Car_Price, car_Horsepower], axis=0)

# join happens on index and there should be no common column
result_df = Car_Price.join(car_Horsepower, how='inner')

# merge and concat can happen on two tables on differnt shapes also
