def kwargs_test(a, b):
    print(a, b)


dct = {'a': 1, "b": 2}
kwargs_test(**dct)

# _______________________________________________________________

my_list = (1, 2, 3, 4)
print(*my_list)


# _______________________________________________________________

def fun(a, b, c, d):
    print(a, b, c, d)


my_list = (1, 2, 3, 4)
print(*my_list)
# my_list = [1, 2, 3, 4]
fun(*my_list)


# _______________________________________________________________

def kwargs_test(a, b):
    print(a, b)


kwargs_test(a=1, b=2)


# _______________________________________________________________

def kwargs_test(**kwargs):
    print(kwargs["a"], kwargs["b"])


kwargs_test(a=1, b=2)


# _______________________________________________________________


def kwargs_test(**kwargs):
    print(kwargs["a"], kwargs["b"])


dct = {'a': 1, "b": 2}
kwargs_test(**dct)
