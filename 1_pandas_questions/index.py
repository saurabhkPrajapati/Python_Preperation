# import numpy and pandas module
import pandas as pd
import numpy as np

column=['a','b','c','d','e']
index=['A','B','C','D','E']

#create a dataframe of random values of array
df1 = pd.DataFrame(np.random.rand(5,5),
		columns=column, index=index)

column=['e','a','b','c','d']
index = ['E', 'A','B','C','D']

# create the new index for columns
print(df1.reindex(column, axis='columns'))
print(df1.reindex(index, axis='rows'))



