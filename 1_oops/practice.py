class Animal:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def create(name, kind):
        if kind == 'dog':
            return Dog(name)
        elif kind == 'cat':
            return Cat(name)
        else:
            raise ValueError("Unknown kind of animal.")

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

animal1 = Animal.create("Bruno", "dog")
animal2 = Animal.create("Milo", "cat")

print(animal1.speak())  # Bruno says Woof!
print(animal2.speak())  # Milo says Meow!
