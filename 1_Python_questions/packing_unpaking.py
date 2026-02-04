def decorator_func(a, *kwargs):
    print(kwargs)


decorator_func(1, {"a": 1, "b": 2}, 2)
decorator_func(1, *{"a": 1, "b": 2}, 2)

# _________________________________
y = [*{'a': 1, 'b': 2}]  # not works with tuple
z = [*{'a': 1, 'b': 2}.items()]  # not works with tuple

l, m, *n = (10, "Geeks ", " for ", "Geeks ", 50)
print(l)
print(m)
print(n)

l, *m, n = (10, "Geeks ", " for ", "Geeks ", 50)
print(l)
print(m)
print(n)


# ___________________________________

def decorator_func(*args, **kwargs):
    print(kwargs)


decorator_func(1, 2, 3, **{"a": 1, "b": 2})


# ___________________________________

def decorator_func(a, b):
    print(b)


decorator_func(1, {"a": 1, "b": 2})


def decorator_func(**kwargs):
    print(kwargs)


decorator_func(a=1, b=2)
