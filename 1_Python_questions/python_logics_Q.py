import sys

print(sys.version)

# _________________________________________________________

# description of Python built-in function(s).
print(sorted.__doc__)
print(len.__doc__)

# _________________________________________________________

import calendar

print(calendar.calendar(2024))  # calender fro 2024
print(calendar.month(2024, 8))  # calendar for month August
print(calendar.isleap(2024))  # True
print(calendar.leapdays(2000, 2024))  # 6 (2000 is included, 2024 is not)

# _________________________________________________________

# Write a Python program to test whether a number is within 100 of 1000 or 2000.

((abs(1000 - 800) <= 100) or (abs(2000 - 800) <= 100))

# Write a Python program to create a histogram from a given list of integers
for i in [2, 3, 6, 5]:
    print("*" * i)

# _____________________________________________________________________________________________________________________

# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
# Input: W3resource Python, Exercises.
# Output: [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]

import re

input = "W3resource Python, Exercises"
merged = re.split(r"([ ,]+)", input)
print([merged[::2], merged[1::2]])

# _____________________________________________________________________________________________________________________


def test(combined):
    ls = []

    s2 = ""

    for s in combined.replace(' ', ''):
        s2 += s

        if s2.count("(") == s2.count(")"):
            ls.append(s2)
            s2 = ""
    return ls


combined = '() (( ( )() (  )) ) ( ())'

print(test(combined))

# _____________________________________________________________________________________________________________________

# Write a Python program to find the longest string in a given list of strings.
input = ['cat', 'car', 'fear', 'center']
dct = dict()
for i in input:
    dct[i] = len(i)
dct_sorting = list(dct.items())
print(sorted(dct_sorting, key=lambda item: item[1], reverse=True)[0][0])

# _____________________________________________________________________________________________________________________

# An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row.
# Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.
# Write a  Python program to find the indices of all occurrences of target in the uneven matrix.

input = [[1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]]
for key, val in enumerate(input):
    if val:
        for key_1, val_1 in enumerate(val):
            if val_1 == 19:
                print(key, key_1)

# _____________________________________________________________________________________________________________________

# Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.

input = [1, 2, 33, 4, 5, 6]
if all([True if input[i + 1] > input[i] else False for i in range(len(input) - 1)]):
    print("Increasing")
elif all([True if input[i + 1] < input[i] else False for i in range(len(input) - 1)]):
    print("Decreasing")
else:
    print('Not Monotonic')

# _____________________________________________________________________________________________________________________

# Write a  Python program to create a list whose ith element is the maximum of the first i elements from an input list.
# Input:
# [1, 19, 5, 15, 5, 25, 5]
# Output:
# [1, 19, 19, 19, 19, 25, 25]

input = [1, 19, 5, 15, 5, 25, 5]

lst = []
for i in range(1, len(input)+1):
    lst.append(max(input[:i]))
print(lst)

# ________________________________________________________________________________________________________________________

# Write a Python program to find the largest integer divisor of a number n that is less than n.

input = 500

for i in range(input-1, 0, -1):
    if input%i == 0:
        print(i)
        break

# ________________________________________________________________________________________________________________________

nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sorted(nums, key=lambda item: sum(int(item) for i in str(item)))
# sorted(nums, key=lambda item: sum((map(int, list(str(item))))))
# ________________________________________________________________________________________________________________________

import base64

base64_html_text = (
    """ICAgIDxodG1sPgogICAgICAgIDxib2R5PgogICAgICAgICAgICA8aDM+SGVsbG8sPC9oMz4KICAg\nICAgICAgICAgPHA+Um91dGU1MyBoYXMgZGV0ZWN0ZWQgdGhhdCB0aGUgYWxhcm0gPGI+S2lvbl9D\nVk9fRG93bjwvYj4gaGFzIGVudGVyZWQgaW4gQUxBUk0gc3RhdGUuIFRoZSBhbGFybSBpcyB0cmln\nZ2VyZWQgYWZ0ZXIgNSBtaW51dCBvZiB3ZWJzaXRlIHVuYXZhaWxhYmlsaXR5LjwvcD4KICAgICAg\nICAgICAgPHA+WW91IGNhbiB2aWV3IHRoZSBncmFwaCBpbiBDbG91ZFdhdGNoIDxhIGhyZWY9Imh0\ndHBzOi8vdXMtZWFzdC0xLmNvbnNvbGUuYXdzLmFtYXpvbi5jb20vY2xvdWR3YXRjaC9ob21lP3Jl\nZ2lvbj11cy1lYXN0LTEjZGFzaGJvYXJkczpuYW1lPTQtV2Vic2l0ZS1Nb25pdG9yaW5nIiB0YXJn\nZXQ9Il9ibGFuayI+aGVyZTwvYT4uPC9wPgogICAgICAgICAgICA8cD5HbG9iYWwgSVQ8L3A+CiAg\nICAgICAgPC9ib2R5PgogICAgPC9odG1sPgogICAg"""
)

html_text = base64.b64decode(base64_html_text).decode('utf-8')

print("\nHTML Version:")
print(html_text)

