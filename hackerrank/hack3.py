import numpy
N = tuple(map(int, input().split()))
print(N)
print(numpy.zeros(N, dtype=numpy.int))  # N= 3 ,3 , 3
print(numpy.ones(N, dtype=numpy.int))

