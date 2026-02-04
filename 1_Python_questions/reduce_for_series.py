from functools import reduce


def subtract(a, b):
    return a - b


numbers = [100, 10, 5, 1, 2, 7, 5]
reduce(subtract, numbers)
# Above we subtracted 10, 5, 1, 2, 7 and 5 from 100.

