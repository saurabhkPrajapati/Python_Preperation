"""
✅ Memory Efficiency
Iterators and generators don’t store the whole dataset in memory.
Example: iterating over a 1 GB log file line by line without loading it entirely.

✅ Lazy Evaluation
Values are produced only when needed.
Useful when dealing with infinite sequences or large datasets.
"""



"""
A generator is a special kind of iterator.
Defined with yield instead of return inside a function, OR created via a generator expression.
Produces values lazily — generates the next value only when requested.
Automatically implements the iterator protocol (__iter__) for you.
"""


"""
Why Generators Are Often Preferred:
    Less code → fewer bugs.
    Automatic handling of the iterator protocol.
    Naturally lazy — doesn’t store entire sequence in memory.
    Good for pipelines, streaming data, infinite sequences.
"""

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
