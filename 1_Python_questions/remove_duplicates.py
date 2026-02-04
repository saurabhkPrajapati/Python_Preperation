from copy import deepcopy


def remove_duplicates(numbers):
    num2 = deepcopy(numbers)
    lst = []
    for i in num2:
        if numbers.count(i) != 1:
            while i in numbers:
                numbers.remove(i)
    return numbers


def remove_duplicates(numbers):
    lst = []
    for i in numbers:
        if numbers.count(i) == 1:
            lst.append(i)
    return lst


nums = [1, 2, 3, 2, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(unique_nums)

# ___________________________________________________


input_string = "geeksforgeek"

result = ""

for char in input_string:
    if char not in result:
        result += char

print(result)


# ______________________________________________________

def duplicate(input_list):
    return list(([x for x in set(input_list) if input_list.count(x) > 1]))


if __name__ == '__main__':
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    print(duplicate(input_list))

############
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = []
y = []
for i in lis:
    if i not in x:
        x.append(i)
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print(y)
