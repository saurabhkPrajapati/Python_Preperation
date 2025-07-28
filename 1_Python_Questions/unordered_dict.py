from collections import OrderedDict

# Create an ordered dictionary of key-value pairs
my_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Add a new item to the end of the dictionary
my_dict['d'] = 4

# Add a new item at a specific position in the dictionary
my_dict.update({'e': 5})
my_dict.update([('f', 6)])

my_dict.move_to_end('e', last=False)

# Iterate over the dictionary in the order in which items were added
for key, value in my_dict.items():
    print(key, value)