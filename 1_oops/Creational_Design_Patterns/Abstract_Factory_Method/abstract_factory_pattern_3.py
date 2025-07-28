from abc import ABC, abstractmethod


# Abstract Factory
class AbstractCarFactory(ABC):
    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_suv(self):
        pass


# Concrete Factory 1
class FordCarFactory(AbstractCarFactory):
    def create_sedan(self):
        return FordSedan()

    def create_suv(self):
        return FordSUV()


# Concrete Factory 2
class ToyotaCarFactory(AbstractCarFactory):
    def create_sedan(self):
        return ToyotaSedan()

    def create_suv(self):
        return ToyotaSUV()


# Abstract Products
class Sedan(ABC):
    @abstractmethod
    def drive(self):
        pass


# Abstract Products
class SUV(ABC):
    @abstractmethod
    def drive(self):
        pass


# Concrete Products
class FordSedan(Sedan):
    def drive(self):
        return "Driving Ford Sedan"


class FordSUV(SUV):
    def drive(self):
        return "Driving Ford SUV"


class ToyotaSedan(Sedan):
    def drive(self):
        return "Driving Toyota Sedan"


class ToyotaSUV(SUV):
    def drive(self):
        return "Driving Toyota SUV"


# Client Code
class CarShop:
    def __init__(self, factory):
        self.factory = factory

    def order_car(self):
        sedan = self.factory.create_sedan()
        suv = self.factory.create_suv()
        return sedan.drive(), suv.drive()


# Usage
ford_factory = FordCarFactory()
toyota_factory = ToyotaCarFactory()

ford_shop = CarShop(ford_factory)
print(ford_shop.order_car())  # Output: ('Driving Ford Sedan', 'Driving Ford SUV')

toyota_shop = CarShop(toyota_factory)
print(toyota_shop.order_car())  # Output: ('Driving Toyota Sedan', 'Driving Toyota SUV')
