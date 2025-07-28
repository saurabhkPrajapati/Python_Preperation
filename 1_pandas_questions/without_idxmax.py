import pandas as pd

reviews = pd.DataFrame({
    'points': [85, 90, 88, 92, 87],
    'price': [10, 15, 8, 20, 12],
    'title': ['Wine A', 'Wine B', 'Wine C', 'Wine D', 'Wine E']
})
reviews['ratio'] = reviews['points'] / reviews['price']
sorted_reviews = reviews.sort_values(by='ratio', ascending=False)
bargain_wine = sorted_reviews.iloc[0]['title']
print(bargain_wine)

# (reviews['points'] / reviews['price']).idxmax()


# def stars(row):
#     if row.country == 'Canada':
#         return 3
#     elif row.points >= 95:
#         return 3
#     elif row.points >= 85:
#         return 2
#     else:
#         return 1
#
# star_ratings = reviews.apply(stars, axis='columns')
