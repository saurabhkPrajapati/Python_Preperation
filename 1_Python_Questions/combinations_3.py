def get_combinations(arr, start=0, length=4, current_combination=[]):
    if len(current_combination) == length:
        print(current_combination)
        return
    if start == len(arr):
        return

    # Include the current element in the combination
    current_combination.append(arr[start])
    get_combinations(arr, start + 1, length, current_combination)

    # Exclude the current element from the combination
    current_combination.pop()
    get_combinations(arr, start + 1, length, current_combination)


# Example usage:
input_list = ["A", "B", "C", "D"]
get_combinations(input_list, length=2)
