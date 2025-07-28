# Inner_Loop: For each position in the outer loop, find the minimum element in the unsorted portion of the array.
# Outer_Loop: Swap the found minimum element with the element at the current position in the outer loop.

# Description: Divides the list into a sorted and an unsorted region
# Repeatedly selects the smallest (or largest) element from the unsorted region in each iteration and  move it to the sorted region.

# Time Complexity: O(n^2)


def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Example usage:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)
