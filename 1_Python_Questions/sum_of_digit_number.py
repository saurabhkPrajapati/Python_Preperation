from functools import reduce

test_list = [12, 67, 98, 34]

print("The original list is : " + str(test_list))
res = list(map(lambda x: sum(int(i) for i in str(x)), test_list))
res = [reduce(lambda a, b: int(a)+int(b), list(str(i))) for i in test_list]
print("List Integer Summation : ", res)

####
mul = reduce(lambda a, b: a*b, test_list)

min = test_list[0]
for i in test_list:
    if i < min:
        min = i
reduce(lambda a, b: a if a > b else b, test_list)
####



