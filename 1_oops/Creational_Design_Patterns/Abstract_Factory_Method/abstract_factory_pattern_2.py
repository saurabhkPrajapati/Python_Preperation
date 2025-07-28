from abc import ABC, abstractmethod


# Abstract Product
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass


# Concrete Products
class Sedan(Car):
    def drive(self):
        return "Driving Sedan"


class SUV(Car):
    def drive(self):
        return "Driving SUV"


# Abstract Factory
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


# Concrete Factories
class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()


class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()


# Client
class CarShop:
    def __init__(self, factory):
        self.factory = factory

    def order_car(self):
        car = self.factory.create_car()
        return car.drive()


# Usage
sedan_shop = CarShop(SedanFactory())
print(sedan_shop.order_car())  # Output: Driving Sedan

suv_shop = CarShop(SUVFactory())
print(suv_shop.order_car())  # Output: Driving SUV
