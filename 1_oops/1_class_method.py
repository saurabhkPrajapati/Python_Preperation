"""
A class method is bound to the class and not the object of the class. It can access only class variables.
class variable are shared between objects
class variable can be access from instance method and class method
"""

class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        # class_name.class_variable
        Student.school_name = school_name

    # instance method
    def show(self):
        print(Student.school_name)
        print({'name': self.name, 'age': self.age, 'School:': Student.school_name})


jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('XYZ School')
jessa.show()
