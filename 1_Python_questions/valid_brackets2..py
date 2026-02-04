def is_valid_brackets(s):
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets.keys():
            s = s.replace(char, '', 1)
            s = s.replace(brackets[char], '', 1)

    return len(s) == 0


# Example usage:
input_str = "({}[)"
if is_valid_brackets(input_str):
    print("Valid brackets")
else:
    print("Invalid brackets")


#
# def is_valid_brackets_counter(s):
#     brackets = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
#
#     for char in s:
#         if char in brackets:
#             brackets[char] += 1
#             if brackets[')'] > brackets['('] or brackets[']'] > brackets['['] or brackets['}'] > brackets['{']:
#                 return False
#
#     return all(brackets[char] == 0 for char in brackets)

# Example usage:
# input_str = "({[]})"
# if is_valid_brackets_counter(input_str):
#     print("Valid brackets")
# else:
#     print("Invalid brackets")

