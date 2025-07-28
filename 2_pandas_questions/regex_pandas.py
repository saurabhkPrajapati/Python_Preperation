# import the regex library
import pandas as pd
import re

# Create a list with all the strings
movie_data = ["Name: The Godfather Year: 1972 Rating: 9.2",
              "Name: Bird Box Year: 2018 Rating: 6.8",
              "Name: Fight Club Year: 1999 Rating: 8.8"]

# Create a dictionary with the required columns
# Used later to convert to DataFrame
movies = {"Name": [], "Year": [], "Rating": []}

for item in movie_data:

    # For Name field
    name_field = re.search("Name: .*", item)

    if name_field is not None:
        name = re.search('Name:\s([a-z]+\s[a-z]+)', name_field.group(), flags=re.IGNORECASE)
    else:
        name = None
    movies["Name"].append(name.group(1))

    # For Year field
    year_field = re.search("Year: .*", item)
    if year_field is not None:
        year = re.search('\s\d\d\d\d', year_field.group())
    else:
        year = None
    movies["Year"].append(year.group().strip())

    # For rating field
    rating_field = re.search("Rating: .*", item)
    if rating_field is not None:
        rating = re.search('\s\d.\d', rating_field.group())
    else:
        rating = None
    movies["Rating"].append(rating.group().strip())

# Creating DataFrame
df = pd.DataFrame(movies)
print(df)
