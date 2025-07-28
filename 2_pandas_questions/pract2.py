import pandas as pd

data = {
    "name": ["John", "Ted", "Dev", "Brad", "Rex", "Smith", "Samuel", "David"],
    "salary": [10000, 20000, 50000, 45500, 19800, 95000, 5000, 50000]
}
# create dataframe from data dictionary
df = pd.DataFrame(data)


# print the dataframe


# Print the DataFrame after
# addition of new column
def salary_stats(value):
    if value < 10000:
        return "very low"
    if 10000 <= value < 25000:
        return "low"
    elif 25000 <= value < 40000:
        return "average"
    elif 40000 <= value < 50000:
        return "better"
    elif value >= 50000:
        return "very good"


df['salary_stats'] = df['salary'].apply(salary_stats)
df['salary_stats'] = df['salary'].map(salary_stats)
print(df.head())
