n1, n2 = 0, 1
nterms = 20


def test(n1, n2):
    count = 0
    fib_seq = []

    while count < nterms:
        fib_seq.append(n1)
        n1, n2 = n2, n1 + n2
        count += 1


test(n1, n2)


# _____________________________________________________________________

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        result = recur_fibo(n - 1) + recur_fibo(n - 2)
        return result
    # take input from the user


nterms = 5
print("Fibonacci sequence:")
for i in range(nterms):
    print(recur_fibo(i))


# ___________________________________________________________________________
# using recurssion and generator
def recur_fibonaci(term):
    if term <= 1:
        yield term
    else:
        result = next(recur_fibonaci(term - 1)) + next(recur_fibonaci(term - 2))
        yield result


for i in range(20):
    print(next(recur_fibonaci(i)))
