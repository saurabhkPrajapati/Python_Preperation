def get_permutations(string, start=0, length=2):
    if start == length:
        print("".join(string[:length]))
    else:
        for i in range(start, len(string)):
            string[start], string[i] = string[i], string[start]  # Swap the characters
            get_permutations(string, start + 1, length)  # Recursively generate permutations for the rest of the string
            string[start], string[i] = string[i], string[start]  # Swap back to the original order


# Example usage:
input_string = "ABCDE"
input_list = list(input_string)
get_permutations(input_list, length=5)
