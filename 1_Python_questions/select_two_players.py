a = [1, 2, 3, 4, 5]

pairs = []

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        pair = (a[i], a[j])
        pairs.append(pair)

print(pairs)
