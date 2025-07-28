# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

from collections import Counter, OrderedDict, defaultdict

order_dict = OrderedDict()

total_products = 1

for i in range(total_products):
    name, _, price = input().rpartition(" ")  # it should read the input
    order_dict[name] = order_dict.get(name, 0) + int(price)

for key, val in order_dict.items():
    print(key, val)

# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
