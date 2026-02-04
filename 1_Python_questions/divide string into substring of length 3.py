# divide string into substring of length 3
lst = []
count = 0
string = "ABCDCDCAA"
for i in range(0, len(string), 3):
    lst.append(string[i:i + 3])

print(lst)

