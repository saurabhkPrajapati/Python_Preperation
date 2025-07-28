import pandas as pd
import numpy as np

technologies = ({
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Hadoop", "Hadoop", "Spark", "Python", np.nan],
    'Fee': [25000, 25000, 23000, 24000, 26000, 25000, 25000, 22000, 1500],
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '30days', '50days', '40days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, None, 1400, 1600, 0]
})

df = pd.DataFrame(technologies)
print(df)

# Using apply() & lambda
# sort_values dont apply on group_by directly >>> df.groupby('Courses').sort_values(by='Fee')
df1 = df.groupby('Courses')
df1.get_group('Hadoop')
df1_count = df.groupby('Courses')['Courses'].count()
df1_count = df.groupby(['Courses', 'Fee']).size().sort_values(ascending=False)
df1_count1 = df.groupby(['Courses', 'Fee'])['Duration'].count().sort_values(ascending=False)
df1_count1 = df.groupby(['Courses', 'Fee'])['Fee'].count().sort_values(ascending=False)
df1 = df.groupby('Courses').apply(lambda x: x.sort_values('Fee'))
print(df1)

# Sorting group keys on descending order
groupedDF = df.groupby('Courses', sort=False).agg(['sum'])
groupedDF = df.groupby('Courses', sort=False)['Fee'].agg(['sum'])
sortedDF = groupedDF.sort_values(by='Fee')
print(sortedDF)
