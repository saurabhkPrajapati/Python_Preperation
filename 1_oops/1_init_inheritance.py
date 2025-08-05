"""
In Python, Employee(object) is defining a class named Employee that inherits from the built-in object class. This
syntax is specific to Python 2, where explicitly inheriting from object is a common practice to create new-style
classes. In Python 3, all classes are new-style by default, so you can simply write class Employee: without
explicitly inheriting from object.

Old-style classes: These were the default in Python 2 if you defined a class without explicitly inheriting from object.

New-style classes: Introduced in Python 2.2, they are created by explicitly inheriting from the built-in object class.
""" 

class Employee:  # Old-style class in Python 2
    pass



class Employee(object):  # New-style class in Python 2
    pass

"""Inheriting from object ensures that the class has modern features like descriptors, properties, and super().

In Python 3, the distinction between old-style and new-style classes was removed.
All classes automatically inherit from object, even if you don't explicitly state it."""

# Therefore, in Python 3, the following two definitions are equivalent:

# Both are new-style classes in Python 3
class Employee:
    pass

class Employee(object):
    pass


# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(
            {
                "name": self.name,
                "idnumber": self.idnumber
            }
        )


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        # super().__init__(name, idnumber)
        Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
