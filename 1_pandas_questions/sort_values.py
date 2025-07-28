import pandas as pd

# create dataframe
data = {'name': ['Simon', 'Marsh', 'Gaurav', 'Alex', 'Selena'],
        'Maths': [8, 5, 5, 5, 7],
        'Science': [7, 9, 5, 4, 7],
        'English': [7, 4, 7, 6, 8]}

df = pd.DataFrame(data)

# Sort the dataframe’s rows by Maths
# and then by English, in ascending order
b = df.sort_values(by=['Maths', 'English'], ascending=[True, False])
