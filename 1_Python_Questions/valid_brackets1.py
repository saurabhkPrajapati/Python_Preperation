def is_valid_brackets(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0


# Example usage:
input_str = "({}[])"
if is_valid_brackets(input_str):
    print("Valid brackets")
else:
    print("Invalid brackets")



import re


def is_valid_brackets_regex(s):
    pattern = r"\(\)|\[\]|\{\}"
    while re.search(pattern, s):
        s = re.sub(pattern, "", s)
    return not s


# Example usage:
input_str = "({}[[]])"
if is_valid_brackets_regex(input_str):
    print("Valid brackets")
else:
    print("Invalid brackets")
