import numpy
numpy.set_printoptions(legacy='1.13')
N = tuple(map(int, input().split()))
print(N)
# print(numpy.eye(N[0], N[1], k=0, dtype=numpy.int))  #eye is always two dimentionaland disgosnl not fixed
print(numpy.identity(N[0], dtype=numpy.int))  #identity can be any dimentional and diagoanl is fixed

