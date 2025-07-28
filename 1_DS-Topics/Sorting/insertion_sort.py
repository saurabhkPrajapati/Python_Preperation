# Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list
# into its correct position in a sorted portion of the list.It is a stable sorting algorithm

# Time Complexity: O(n^2)


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])
