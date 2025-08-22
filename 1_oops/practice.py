def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    for i in range(n+1):
        count += 1
        n1, n2 = n2, n1+n2
        yield n1

# x = fibonacci(10)
# print(next(x))
# print(next(x))
# print(next(x))

def fib(n):
    if n <= 1:
        return n
    if n <= 0:
        return 0
    return fib(n-1) + fib(n-2)

num_terms = 10
print(f"Fibonacci series up to {num_terms} terms:")
for i in range(num_terms):
    print(fib(i), end=" ")