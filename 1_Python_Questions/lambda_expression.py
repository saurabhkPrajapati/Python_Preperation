import functools

print((lambda x, y: (x > y and x) or y)(5, 6))

# type annotations does not work

print(lambda arg=x: arg * 10 for x in range(1, 5))
(lambda x, y, z=3: x + y + z)(1, y=2)
(lambda *args: sum(args))(1, 2, 3)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)
(lambda x, y, z: x + y + z)(1, 2, 4)

(lambda *args, **kwargs: sum(args) + sum(kwargs.values()))(1, 2, 3, one=1, two=2, three=3)

# A decorator can be applied to a lambda.
# Although it’s not possible to decorate a lambda with the @decorator syntax,
# a decorator is just a function, so it can call the lambda function:


ages = [13, 90, 17, 59, 21, 60, 5]
list(filter(lambda age: age > 18, ages))

# seconds largest
List = [[3, 5, 4], [1, 4, 67, 64], [3, 6, 9, 12]]
sort_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, sort_func: [y[len(y) - 2] for y in sort_func(x)]
res = second_largest(List, sort_list)

square = lambda x: x ** 2
product = lambda func, n: lambda x: func(x) * n
ans = product(square, 2)(10)
print(ans)

x = lambda a=1, b=3: lambda c: a + b + c
y = x(1, 2)(4)
print(y)

square = lambda x: x ** 2
product = lambda val: lambda pow: lambda y: y ** pow * val
ans = product(val=2)(pow=3)(y=4)
print(ans)

lis = [166, 3, 57, 26, 2, ]
print(functools.reduce(lambda a, b: (a > b and a) or b, lis))

# __________________________________________________________________________________


# If you modify the expression to is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)],
# it introduces a default argument arg=x in the lambda function. This allows each lambda function to capture the value of x at the
# time of creation.
#
# To retrieve the values of is_even_list using this modified expression,
# you can execute each lambda function without passing any arguments. Here's an example:
# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())

# The expression is_even_list = [lambda x: x * 10 for x in range(1, 5)] creates a list of lambda functions. However, the lambda functions themselves are not executed, so the list is_even_list contains the lambda functions, not their values.
#
# To retrieve the values of is_even_list, you can execute each lambda function with a specific input. Here's an example:
#
# python
# Copy code
# is_even_list = [lambda x: x * 10 for x in range(1, 5)]
# values = [func(x) for func, x in zip(is_even_list, range(1, 5))]
# print(values)
#
