import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])

# Adding values
s = Student('Nandini', '19', '2541997')
s1 = Student(name='Nandini', age='19', DOB='2541997')

# initializing iterable
li = Student('Manjeet', '19', '411997')

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))

# _________________________________________________________________________________zz

# importing "collections" for namedtuple()
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])
