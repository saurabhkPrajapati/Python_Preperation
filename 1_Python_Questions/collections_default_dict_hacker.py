# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

input_n, input_m = 5, 2
d = defaultdict(list)
list1 = 'a', 'a', 'b', 'a', 'b'
list2 = 'a', 'b', 'c'
for i, j in list(zip(range(1, input_n + 1), list1)):
    ans1 = j
    d[ans1].append(i)
for j in list2:
    ans2 = j
    if ans2 in d:

        print(*d[ans2])
    else:
        print(-1)

# ___________________________________________________________________________________________

# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import Counter, defaultdict

n = int(input())
l1 = [input().strip() for _ in range(n)]
print(len(set(l1)))
dict_ = defaultdict(int)

for val in l1:
    dict_[val] += 1

print(*(dict_.values()))
