from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def calculate_risk(self):
        pass


# Concrete class
class Worker(Product):
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours

    def calculate_risk(self):
        # Please imagine a more plausible implementation
        return self.age + 100 / self.hours

    def __str__(self):
        return self.name + " [" + str(self.age) + "] - " + str(self.hours) + "h/week"


# Concrete class
class Unemployed(Product):
    def __init__(self, name, age, able):
        self.name = name
        self.age = age
        self.able = able

    def calculate_risk(self):
        # Please imagine a more plausible implementation
        if self.able:
            return self.age + 10
        else:
            return self.age + 30

    def __str__(self):
        if self.able:
            return self.name + " [" + str(self.age) + "] - able to work"
        else:
            return self.name + " [" + str(self.age) + "] - unable to work"


# Define the Creator (Factory) class
class PersonFactory:

    @staticmethod
    def get_person(type_of_person, name, age, hours_or_able):
        localizers = {
            "Worker": Worker,
            "Unemployed": Unemployed,
        }

        return localizers[type_of_person](name, age, hours_or_able)


print(PersonFactory.get_person('Worker', 'Ravi', 27, 4))
print(PersonFactory.get_person('Unemployed', 'Ravi', 27, False))
