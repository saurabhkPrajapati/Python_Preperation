# An iterator in Python is an object that is used to iterate over iterable objects ********************
# like lists, tuples, dicts, and sets. The Python iterators object is initialized using the iter() method.
# It uses the next() method for iteration.

# __iter__(): initializes the starting point of the iteration and returns the iterator object itself.

# Memory Efficiency
# Iterators allow you to work with sequences of data without loading the entire dataset into memory.
# Instead of creating a list or another collection that stores all items at once, an iterator generates items one at a time.
# This makes iterators ideal for processing large datasets or streams
with open('large_file.txt') as file:
    for line in file:
        process(line)  # Handle one line at a time

# Lazy Evaluation
# Iterators compute values on demand (lazily) rather than computing everything upfront.
# This means that operations are only performed when needed, improving performance for scenarios where only a portion of the data may be consumed.

for num in range(1_000_000):  # Efficiently handles large ranges
    if num > 10:
        break  # Stops early without generating all numbers


class Test:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= self.limit:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


for i in Test(5):
    print(i)

#############################################################

v = iter(Test(5))
for i in v:
    print(i)

#############################################################

tup = ('a', 'b', 'c', 'd', 'e')

# creating an iterator from the tuple
tup_iter = iter(tup)

print("Inside loop:")
# iterating on each item of the iterator object
for index, item in enumerate(tup_iter):
    print(item)

    # break outside loop after iterating on 3 elements
    if index == 2:
        break

# we can print the remaining items to be iterated using next()
# thus, the state was saved
print("Outside loop:")
print(next(tup_iter))
print(next(tup_iter))
