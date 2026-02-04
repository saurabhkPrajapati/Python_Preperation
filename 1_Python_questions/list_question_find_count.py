# find the count of words in list that start with "particular words"
from functools import reduce

# Initializing list
test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

# Initializing substring
test_sub = 'gfg'

# using lambda function to check if a string starts with the given substring
count_func = lambda count, string: count + 1 if string.startswith(test_sub) else count

# using reduce() function to apply the lambda function to each element of the list
res = reduce(count_func, test_list, 0)

# printing original list
print("The original list is : " + str(test_list))

# printing result
print("Strings count with matching frequency : " + str(res))
