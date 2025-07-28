from itertools import combinations, permutations, combinations_with_replacement, groupby

string, size = "HACK 2".split()

combinations_list = sorted(combinations(string, int(1)))
combinations_list.extend(combinations(sorted(string), int(size)))
for val in combinations_list:
    print("".join(val))

print("\n\n")

# _____________________________________________________________________________________________________________________________

# Combination with replacement

from itertools import combinations_with_replacement

string, size = "HACK 2".split()
combinations_list = combinations_with_replacement(sorted(string), int(size))
for val in combinations_list:
    print("".join(val))

# _____________________________________________________________________________________________________________________________


# Question Link: https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true


from itertools import combinations, groupby

# Read the input
count, letters, to_select = 4, "a a c d".split(), 2

# sort the letters so all a's are on left side
letters = sorted(letters)

# Find all possible combinations of to_select
combinations_of_letters = list(combinations(letters, to_select))

# find all which contain
contain = len([c for c in combinations_of_letters if 'a' in c])

# Print Results
print(contain / len(combinations_of_letters))
