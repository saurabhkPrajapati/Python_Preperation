data = {1: 'a', 2: 'a', 3: 'b'}
result = {}

for key, value in data.items():
    if value in result:
        result[value].append(key)
    else:
        result[value] = [key]

print(result)

# ___________________________________________________

data = {1: 'a', 2: 'a', 3: 'b'}
result = {}

for key, value in data.items():
    result.setdefault(value, []).append(key)

print(result)  # Output: {'a': [1, 2], 'b': [3]}

# ___________________________________________________

from collections import defaultdict

data = {1: 'a', 2: 'a', 3: 'b'}
result = defaultdict(list)

for key, value in data.items():
    result[value].append(key)

print(dict(result))

