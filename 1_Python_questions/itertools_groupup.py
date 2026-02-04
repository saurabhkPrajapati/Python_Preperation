from itertools import groupby

for k, c in groupby("1222311"):
    print((int(len(list(c))), int(k)), end=" ")
