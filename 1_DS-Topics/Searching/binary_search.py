# Binary search is a more efficient algorithm but requires the list to be sorted.
# It repeatedly divides the search interval in half and compares the target value to the middle element of the array.
# If the target is less than the middle element, repeat the process with the low half.
# If the target is greater, repeat the process with the high half.


# Binary Search in python


def binary_search(array, target, low, high):
    # Repeat until the pointers low and high meet each other
    while low <= high:

        # mid = low + (high - low) // 2
        mid = (low + high) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:  # If target is greater, ignore left half
            low = mid + 1

        else:  # If target is lower, ignore right half
            high = mid - 1

    return -1


array_1 = [3, 4, 5, 6, 7, 8, 9, 10, 34, 78]
target_val = 34

result = binary_search(array_1, target_val, 0, len(array_1) - 1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
