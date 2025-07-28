# Quick Sort is an efficient, in-place, divide-and-conquer sorting algorithm.
# It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays,
# according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

# Time Complexity: O(n log n)

# https://www.geeksforgeeks.org/quick-sort-algorithm/


def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as pivot
    i = low - 1  # Pointer for the greater element

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Example usage:
arr_ = [10, 80, 30, 90, 40, 50, 70]
n = len(arr_)
quick_sort(arr_, 0, n - 1)
print("Sorted array is:", arr_)
