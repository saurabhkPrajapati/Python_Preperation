test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print("The original list is : " + str(test_list))

# res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
res = [sub.replace('e', '-').replace('G', 'e').replace('-', 'G') for sub in test_list]

print("List after performing character swaps : " + str(res))
