from copy import deepcopy, copy

round1 = [1, 2]
round2 = copy(round1)
list(zip(round1, round2))
print([[id(i), id(j)] for i, j in zip(round1, round2)])

# gives list of tuples
