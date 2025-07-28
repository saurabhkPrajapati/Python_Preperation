List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

# sort_list = lambda x: [sorted(i) for i in x]
# second_largest = lambda f, x: [y[len(y) - 2] for y in f(x)]
sort_list = lambda x: list(map(lambda i: sorted(i), x))
second_largest = lambda f, x: list(map(lambda y: y[len(y) - 2], f(x)))
res = second_largest(sort_list, List)

print(res)

addition_lambda = lambda x: (lambda y: x + y)
result = addition_lambda(5)(3)
print(result)  # Output will be 8

is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# is_even_list = list(map(lambda x: x*10, [*range(1, 5)]))
for item in is_even_list:
    print(item())

is_even_list = lambda lst: list(map(lambda x: x * 10, lst))
for item in is_even_list([*range(1, 5)]):
    print(item)

# ____________________________________________

num = 12
for num in range(10, 50 + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
