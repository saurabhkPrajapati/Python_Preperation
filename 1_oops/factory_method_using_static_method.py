class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def create_animal(name):
        return Animal(name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Golden Retriever"


# Using static method as a factory method
dog = Dog.create_animal("Buddy")
print(type(dog))  # Outputs: <class '__main__.Animal'>
print(dog.name)  # Outputs: Buddy

# Attempting to access breed will raise an AttributeError because it's an Animal instance, not a Dog.
# print(dog.breed)
