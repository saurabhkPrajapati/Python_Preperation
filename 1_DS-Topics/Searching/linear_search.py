def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1


# Example usage:
arr_1 = [2, 4, 0, 1, 9]
target = 1

result = linear_search(arr_1, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
