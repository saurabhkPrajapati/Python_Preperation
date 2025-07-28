# Description: Repeatedly traverses through the list, compares adjacent elements, and
# swaps them if they are in the wrong order.

# Time Complexity: O(n^2)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


my_list = [64, 34, 25, 12, 22, 11, 90, 80]
bubble_sort(my_list)
print("Sorted array is:", my_list)
