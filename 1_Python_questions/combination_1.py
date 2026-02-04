from itertools import combinations


def get_combinations(data):
    combinations_list = []
    for i in range(len(data) - 2):
        for j in range(i + 1, len(data) - 1):
            for k in range(j + 1, len(data)):
                combinations_list.append((data[i], data[j], data[k]))
    print(combinations_list)


data = [1, 2, 3, 4]
print(list(combinations(data, 3)))

get_combinations(data)
