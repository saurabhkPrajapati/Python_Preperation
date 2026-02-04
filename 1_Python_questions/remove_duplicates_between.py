from copy import deepcopy

a = [5, 2, 3, 4, 5, 6]
b = [5, 6, 7, 5, 5, 8, 9, 10]
a_copy = deepcopy(a)
b_copy = deepcopy(b)
print(id(a), id(b))
for i in a_copy:
    if i in b_copy:
        a.remove(i)

for i in b_copy:
    if i in a_copy:
        b.remove(i)

print(id(a), id(b))
print(a, b)
# ________________________________________________________

a = [5, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 10]
c = [i for i in a if i not in set(b)]
d = [i for i in b if i not in set(a)]
print(id(a), id(b))
print(id(c), id(d))
print(c, d)
