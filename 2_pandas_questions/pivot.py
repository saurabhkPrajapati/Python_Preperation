import pandas as pd

data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'Product': ['A', 'A', 'B', 'A', 'B'],
    'Sales': [100, 100, 150, 120, 200]
}

df = pd.DataFrame(data)
# pivot_df = df.pivot(index='Date', columns='Product', values='Sales')
pivot_table = df.pivot_table(index='Product', values='Sales', aggfunc='sum')

pivot_df = df.pivot_table(index='Date', columns='Product', values='Sales', aggfunc=['sum'])
pivot_df['Total'] = pivot_df.sum(axis=1)
pivot_df1 = df.pivot_table(index='Date', columns='Product', values='Sales', aggfunc=['sum'], margins=True,
                           margins_name='Total')
print(pivot_df1)

# _____________________________________________________


# Create a sample DataFrame
data = {'Date': ['2023-01-01', '2023-02-05', '2023-03-10', '2023-01-15', '2023-02-20', '2023-03-25'],
        'Product': ['A', 'A', 'B', 'A', 'B', 'C'],
        'Sales': [100, 150, 200, 120, 250, 80]}

df = pd.DataFrame(data)

# Convert the 'Date' column to a pandas datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month from the 'Date' column
df['Month'] = df['Date'].dt.month

# Create a pivot table to summarize sales by product and month
pivot_table = df.pivot_table(index=['Product'], columns=['Month'], values='Sales', aggfunc='sum')

# Add a total column
pivot_table['Total'] = pivot_table.sum(axis=1)

print(pivot_table)
