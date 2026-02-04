# For a custom default value like "Not Present": use lambda: "Not Present".
# For an empty string as the default: use defaultdict(str)
# For an empty list as the default: use defaultdict(list)


from collections import Counter, OrderedDict, defaultdict, namedtuple, deque

# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)

# _________________________________________________

# Using str as the factory function
str_defaultdict = defaultdict(str)
str_defaultdict['greeting'] = 'Hello'
print(str_defaultdict["test"])
print(str_defaultdict)

# _________________________________________________

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)
print(d[7])

# _________________________________________________

# Defining the dict and passing
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])
