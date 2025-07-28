# a = ['a', 'b', 'c', 'b', 'c', 'c']
# values_count_dict = {}
# counter = 0
# for i in a:
#     values_count_dict[i] = a.count(i)
#     count = 0
#
# print(values_count_dict)

# ________________________________________________________________________

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            try:
                if arr[j + 1] == 0:
                    arr.append(arr[j + 1])
                    arr.remove(0)
                elif arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            except (Exception,) as e:
                print(e)
        if not swapped:
            return arr


my_list = [64, 0, 34, 0, 0, 0, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array is:", my_list)

# _____________________________________________________________________________________________________

my_list = [64, 0, 34, 0, 0, 0, 25, 12, 22, 11, 90]
non_seros = [i for i in my_list if i != 0]
zeros = [0] * (len(my_list) - len(non_seros))
sorted_non_zero = sorted(non_seros)
sorted_non_zero.extend(zeros)
print(sorted_non_zero)
