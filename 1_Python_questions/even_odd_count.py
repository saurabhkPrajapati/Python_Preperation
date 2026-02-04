list1 = [10, 21, 4, 45, 66, 93]
even, odd = 0, 0
l = list(map(lambda a: 1 if (a%2==0) else 0, list1))
l.count(1)
l.count(0)
####
even1 = list(filter(lambda a: a%2==0, list1))
odd1 = list(filter(lambda a: a%2!=0, list1))
###
even2, odd2 = 0, 0
for i in list1:
    if i % 2 == 0:
        even2 += 1
    else:
        odd2 += 1

even2, odd2 = 0, 0
