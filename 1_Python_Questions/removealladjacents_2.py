def get_ranges(s):
    ranges_list = []
    starts = 0

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            ranges_list.append((s[starts], starts, i - 1))
            starts = i

    ranges_list.append((s[starts], starts, len(s) - 1))

    return ranges_list


input_string = "aaaabbaaccmmdddaeffa"
ranges_lists = get_ranges(input_string)
nw_str = ''
for char, start, end in ranges_lists:
    if start == end:
        nw_str += char

print(nw_str)

# ______________________________________________________________

import re

input_str = "aaaabbaazcczmmaddadaeffa"
pattern = r"(.)\1+"
# input_str = "c mmmmmm"
# pattern = r"(.)(m)\1"

input_str = re.sub(pattern, "", input_str)

print(input_str)
# (aaaa)(bb)(aa)(cc)(mm)a(dd)adae(ff)a
# aadaea
