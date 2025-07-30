"""
A static method is bound to the class (can be called without creating an object) and not the object of the class.
Therefore, we can call it using the class name.

Static methods don’t have access to the class or instance (no cls or self), so they are less suitable for factory methods,
because they cannot easily instantiate or return objects of the class or its subclasses.
Hardcoded class is there, so cannot work dynamically with two subclasses 

Class methods, on the other hand, have access to the class (cls)
and are designed for such scenarios where you might want to return different instances based on class-level logic.
Can call subclasses through cls, so works dynamically for two subclasses

Using a @staticmethod/@classmethod as a factory method in Python is a great way to create alternative constructors for a class

Using @classmethod here provides flexibility, allowing factory_method to return instances of whichever class calls it,
making it ideal for factory methods in inheritance hierarchies.
"""


class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = Employee.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)


emp = Employee('Kelly', 12000, 'ABC Project1')
print(Employee.gather_requirement('ABC Project'))
emp.work()
# call static method with class
