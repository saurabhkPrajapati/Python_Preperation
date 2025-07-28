class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def __init__(self, name, breed):
        # Animal.__init__(self, name)
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")


dog = Dog("Sparky", "Labrador Retriever")
dog.eat()  # Output: Sparky is eating.
dog.bark()  # Output: Sparky is barking.

