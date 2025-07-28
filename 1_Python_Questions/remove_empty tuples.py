def Remove(tuples1):
    tuples1 = filter(None, tuples1)
    return list(tuples1)


tuples1 = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('', ''), ()]

print(Remove(tuples1))
print(list(filter(None, tuples1)))
