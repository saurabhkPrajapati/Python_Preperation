def longest_common_prefix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)
    for i in range(len(shortest_str)):
        char = shortest_str[i]
        for str in strs:
            if str[i] != char:
                return shortest_str[:i]
    return shortest_str


# Test the function
strs = ["flap", "flaap", "flapa"]
result = longest_common_prefix(strs)
print(result)  # Output: fla
