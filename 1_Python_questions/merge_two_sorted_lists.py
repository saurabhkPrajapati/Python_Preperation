lst1 = [4, 6, 8]
lst2 = [5, 7, 9]


def merge(lst1, lst2):
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    elif lst2[0] < lst1[0]:
        return [lst2[0]] + merge(lst1, lst2[1:])


print(merge(lst1, lst2))
