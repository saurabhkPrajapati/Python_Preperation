"""
program to illustrate protected access modifier in a class
protected attributes can be inherited in multilevel inheritance
protected attributes of a parent class can be accessed in the grandchild class or any level of subclassing hierarchy in Python
"""


# super class
class Student:

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected member function
    def _display_roll_and_branch(self):
        # accessing protected data members
        print(
            {
                "Roll": self._roll,
                "Branch": self._branch
            }
        )


# derived class
class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def display_details(self):
        # accessing protected data members of super class
        print("Name: ", self._name)

        # accessing protected member functions of super class
        self._display_roll_and_branch()
        # super()._display_roll_and_branch()


# creating objects of the derived class
obj = Geek("R2J", 1706256, "Information Technology")

# calling public member functions of the class
obj.display_details()
print(obj._name)
