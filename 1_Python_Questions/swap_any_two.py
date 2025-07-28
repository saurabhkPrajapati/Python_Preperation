def swapPositions(list, pos1, pos2):
    # popping both the elements from list
    first_ele = list.pop(pos1-1)
    second_ele = list.pop(pos2-1-1)

    # inserting in each others positions
    list.insert(pos1-1, second_ele)
    list.insert(pos2-1, first_ele)

    return list


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 4
List[pos1-1], List[pos2-1] = List[pos2-1], List[pos1-1]
print(swapPositions(List, pos1, pos2))
