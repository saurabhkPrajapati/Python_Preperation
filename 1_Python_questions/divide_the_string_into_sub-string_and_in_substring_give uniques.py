def merge_the_tools(string, k):
    substrings = []
    clean_substring = []

    for i in range(0, len(string), k):
        substrings.append(string[i: i + k])

    for subs in substrings:
        unique = ""
        for char in subs:
            if char not in unique:
                unique += char
        clean_substring.append(unique)

    return substrings, clean_substring


result = merge_the_tools("AAABCADDE", 3)
print(result)

# When you write clean_substring[key:key+1], you are creating a slice of the list.
# This returns a new list, not a reference to the original list.
# Therefore, calling .append() on this slice does nothing to the actual list.
