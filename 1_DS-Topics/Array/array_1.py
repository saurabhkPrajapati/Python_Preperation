import array
import sys

# arrays in Python cannot directly hold other arrays.
# so appending [11, 22, 33] will not work

# Creating an array of signed integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Extending the array with another array
arr.extend(array.array('i', [6, 7, 8, 6, 6]))
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8])
print(arr.tolist())
# Extending the array with a list
arr.extend([9, 10])
print(arr)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr.count(6))

# _____________________________________________________________________________________________________________

# Example Memory Efficiency

arr = array.array('i', [1, 2, 3, 4, 5])

lst = [1, 2, 3, 4, 5]

print(sys.getsizeof(arr))  # Output: Size of array in bytes

print(sys.getsizeof(lst))  # Output: Size of list in bytes

# _____________________________________________________________________________________________________________

# https://www.simplilearn.com/tutorials/python-tutorial/python-arrays

# _____________________________________________________________________________________________________________
