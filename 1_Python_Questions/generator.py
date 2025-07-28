# Generators yield items one at a time, without storing the entire sequence in memory.

def large_range(n):
    for i in range(n):
        yield i


gen = large_range(10 ** 6)


# _______________________________________________________________________________________

def fibonaci():
    n = 10
    num1, num2 = 0, 1
    count = 1

    while count <= n:
        yield num1
        count += 1
        num1, num2 = num2, num1 + num2


x = fibonaci()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

##################################################################################################

# A generator function in Python is defined like a normal function, but whenever it needs to generate a value,
# it does so with the yield keyword rather than return. If the body of a def contains yield,
# the function automatically becomes a Python generator function.

# generator expression
generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

for i in generator_exp:
    print(i)


# ___________________________________________________________________________

def recur_fibonaci(term):
    if term <= 1:
        yield term
    else:
        result = next(recur_fibonaci(term - 1)) + next(recur_fibonaci(term - 2))
        yield result


for i in range(20):
    print(next(recur_fibonaci(i)))


# _________________________________________________________________

def fibonaci():
    n = 10
    num1, num2 = 0, 1
    count = 1

    while count <= n:
        yield num1
        count += 1
        num1, num2 = num2, num1 + num2


fib = fibonaci()
for num in fib:
    print(num)
