import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
}

df = pd.DataFrame(data)

# Sample specific columns using axis=1
sampled_columns = df.sample(n=1, axis=1)  # You can adjust the number of columns you want to sample
sampled_rows = df.sample(n=3, axis=0)

print(sampled_columns)
print(sampled_rows)
