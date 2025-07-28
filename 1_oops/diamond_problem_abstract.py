# In Python, abstract methods defined in an abstract base class (ABC) serve as a blueprint for what methods
# should be implemented in its subclasses

# If a subclass does not implement an abstract method, attempting to instantiate that subclass will raise a TypeError.

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Mammal(Animal):
    def eat(self):
        print("Mammal is eating.")


class Reptile(Animal):
    def eat(self):
        print("Reptile is eating.")


class Chameleon(Mammal, Reptile):
    def eat(self):
        print("Chameleon is eating.")


chameleon = Chameleon()
chameleon.eat()
