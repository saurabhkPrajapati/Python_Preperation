value = 8
for i in range(1, value+1):
    print()
    print(i*" ", end="")
    if i%2 == 0:
        for j in range(value+1-i, 0, -1):
            print(j, end=" ")
    else:
        for j in range(1, value+2-i):
            print(j, end=" ")

value = 9
# for i in range(value, 0, -1):
for i in range(1, 1+value):
    r = range(1, value+2-i)
    print()
    print(i*" ", end="")
    for j in reversed(r):
        print(j, end=" ")

value = 16
for i in range(1, value+1):
    print()
    print(i*" ", end="")
    for j in range(value+1-i, 0, -1):
        print(j, end=" ")

value = 16
for i in range(value, 0, -1):
    print()
    print(20*" ", i * " ", end="")
    for j in range(value+1-i, 0, -1):
        print(20*"", j, end=" ")


value = 8
for i in range(1, value+1):
# for i in range(value, 0, -1):
    print()
    print(i*" ", end="")
    r = range(1, value+2-i)
    if i%2 == 0:
        for j in reversed(r):
            print(j, end=" ")
    else:
        for j in r:
            print(j, end=" ")

