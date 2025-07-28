import numpy
numpy.set_printoptions(legacy='1.13')

N = tuple(map(int, input().split()))
# M = list(map(int, input().split()))
# L = list(map(int, input().split()))
a = []
b = []
for i in range(N[0]):
    a.append(list(map(int, input().split())))
for i in range(N[0]):
    b.append(list(map(int, input().split())))

a = numpy.array(a, int)
b = numpy.array(b, int)
# a = numpy.array([1, 2, 3, 4], float)
# b = numpy.array([5, 6, 7, 8], float)

print(a + b)                     #[  6.   8.  10.  12.]
print(numpy.add(a, b))           #[  6.   8.  10.  12.]

print(a - b)                     #[-4. -4. -4. -4.]
print(numpy.subtract(a, b))      #[-4. -4. -4. -4.]

print(a * b)                     #[  5.  12.  21.  32.]
print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

print(a / b)                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print(numpy.divide(a, b))        #[ 0.2         0.33333333  0.42857143  0.5       ]
print(numpy.floor_divide(a, b))   #[ 0.2         0.33333333  0.42857143  0.5       ]
a = numpy.divide(0, b, dtype=numpy.int_)

print(a % b)                     #[ 1.  2.  3.  4.]
print(numpy.mod(a, b))           #[ 1.  2.  3.  4.]

print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(numpy.power(a, b))

