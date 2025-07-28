a = [5, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9, 10]
print(id(a), id(b))
a_ind = []
b_ind = []
for i, j in enumerate(a):
    if j in b:
        a_ind.append(i)
for i, j in enumerate(b):
    if j in a:
        b_ind.append(i)
for i in reversed(a_ind):
    a.pop(i)
for i in reversed(b_ind):
    b.pop(i)
# print(a)
# print(b)

print(id(a), id(b))

# The IDs remain the same because the lists were modified in-place, not reassigned to new objects.

# ________________________________________________________________________________________________________________

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True: Values in the lists are the same
print(a is b)  # False: a and b are different objects
print(a is c)  # True: c points to the same object as a
