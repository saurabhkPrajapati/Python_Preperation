ans = "Alicent Wincent".split(' ')
ans1 = [i.capitalize() for i in ans]

# split() vs split(" ")
# s.split() removes extra spaces between words as it collapses multiple spaces into a single space when splitting the string.
# s.split(' ') preserves extra spaces because it explicitly splits on spaces without collapsing them.

s = "12abc"
print(s.title())  # Output: "12Abc"

s = "john o'neill"
print(s.title())  # Output: "John O'Neill", this name is correct though

s = "McDonald's"
print(s.title())  # Output: "Mcdonald'S"

s = "jack-in-the-box"
print(s.title())  # Output: "Jack-In-The-Box"

s = "hello123world"
print(s.title())  # Output: "Hello123World"
