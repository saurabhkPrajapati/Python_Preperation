import numpy
numpy.set_printoptions(legacy='1.13')

N = tuple(map(int, input().split()))
M = list(map(int, input().split()))
L = list(map(int, input().split()))

a = numpy.array([M], int)
b = numpy.array([L], int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.divide(0, b).astype(int))
print(numpy.mod(a, b))
print(numpy.power(a, b))

