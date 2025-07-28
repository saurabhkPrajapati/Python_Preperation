list1 = [1, [2], 3, [[4, 5, [6, 7]]], [8, 9, 10]]
lst = []


def check(list1):
    lst = []
    for i in list1:
        if isinstance(i, int):
            lst.append(i)
        else:
            lst.extend(i)
    checking = any([True for i in lst if isinstance(i, list)])
    if checking:
        return check(lst)
    else:
        return lst


a = check(list1)
print(a)
