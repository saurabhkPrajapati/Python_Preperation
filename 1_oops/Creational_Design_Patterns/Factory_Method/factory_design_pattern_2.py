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
        return f"{self.name} [{self.age}] - {self.hours}h/week"


# Concrete class
class Unemployed(Product):
    def __init__(self, name, age, able, address, phone_number):
        self.name = name
        self.age = age
        self.able = able
        self.address = address
        self.phone_number = phone_number

    def calculate_risk(self):
        # Please imagine a more plausible implementation
        if self.able:
            return self.age + 10
        else:
            return self.age + 30

    def __str__(self):
        if self.able:
            return f"{self.name} [{self.age}] - able to work"
        else:
            return f"{self.name} [{self.age}] - unable to work"


# Define the Creator (Factory) class
class PersonFactory:

    @staticmethod
    def get_person(type_of_person, name, age, hours_or_able, address=None, phone_number=None):
        localizers = {
            "Worker": Worker,
            "Unemployed": Unemployed,
        }

        if type_of_person == "Worker":
            return localizers[type_of_person](name, age, hours_or_able)
        elif type_of_person == "Unemployed":
            return localizers[type_of_person](name, age, hours_or_able, address, phone_number)


# Example usage of the PersonFactory
worker = PersonFactory.get_person("Worker", "John", 30, 40)
print(worker)  # Output: John [30] - 40h/week

unemployed = PersonFactory.get_person("Unemployed", "Alice", 25, False, "123 Main St", "555-1234")
print(unemployed)  # Output: Alice [25] - unable to work
