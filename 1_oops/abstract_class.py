"""
In Python, abstract methods defined in an abstract base class (ABC) serve as a blueprint for what methods
should be implemented in its subclasses

If a subclass does not implement an abstract method, attempting to instantiate that subclass will raise a TypeError.
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    # concrete method
    def sleep(self):
        print("I am going to sleep in a while")

    @abstractmethod
    def sound(self):
        print("This function is for defining the sound by any animal")


class Snake(Animal):
    def sound(self):
        print("I can hiss")


class Dog(Animal):
    def sound(self):
        print("I can bark")


class Lion(Animal):
    pass


class Cat(Animal):
    def sound(self):
        print("I can meow")


c = Cat()
c.sleep()
c.sound()

c = Snake()
c.sound()
c = Lion()
c.sound()
