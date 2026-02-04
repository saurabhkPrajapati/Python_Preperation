from itertools import starmap, accumulate
from functools import reduce

temp = list(starmap(pow, [(2, 7), (4, 3)]))
print(temp)
# temp = list(map(pow, [(2, 7), (4, 3)]))  #pow((2,3)) is  wrong
# print(temp)
temp = list(map(pow, (2, 7), (4, 3)))
print(temp)

# map() and starmap() is that the latter calls its transformation function
# using the unpacking operator (*) to unpack each tuple of arguments into several positional arguments
temp = list(map(lambda x: pow(x[0], x[1]), [(2, 7), (4, 3)]))
print(temp)

li = [(2, 3), (3, 1), (4, 6), (5, 3), (6, 5), (7, 2)]
ans = list(starmap(lambda x, y: x + y, li))
print(ans)

# https://www.geeksforgeeks.org/python-itertools-starmap/
# https://thispointer.com/python-map-function-explained-with-examples/#:~:text=Using%20map()%20function%20to%20transform%20Dictionaries%20in%20Python&text=map()%20function%20iterated%20over,original%20dictionary%20with%20updated%20contents.
# https://thispointer.com/python-filter-a-dictionary-by-conditions-on-keys-or-values/#:~:text=Filter%20a%20Dictionary%20by%20values%20in%20Python%20using%20filter()&text=filter()%20function%20iterates%20above,on%20condition%20passed%20as%20callback.

