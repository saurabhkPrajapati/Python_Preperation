# Imagine a coffee shop where you can order coffee with additional features like milk, sugar, or caramel.
# Instead of creating separate classes for every combination of coffee, we use the decorator pattern.

from abc import ABC, abstractmethod


# Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self):
        """Returns the cost of the coffee."""
        pass

    @abstractmethod
    def description(self):
        """Returns the description of the coffee."""
        pass


# Concrete Component
class BasicCoffee(Coffee):
    def cost(self):
        return 50  # Base cost of a coffee in rupees

    def description(self):
        return "Basic Coffee"


# Decorator (Base Class)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


# Concrete Decorators
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 10  # Adding milk costs 10

    def description(self):
        return self._coffee.description() + ", Milk"


class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 5  # Adding sugar costs 5

    def description(self):
        return self._coffee.description() + ", Sugar"


class Caramel(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 20  # Adding caramel costs 20

    def description(self):
        return self._coffee.description() + ", Caramel"


# Client Code
if __name__ == "__main__":
    # Basic Coffee
    coffee = BasicCoffee()
    print(f"Order: {coffee.description()}")
    print(f"Cost: ₹{coffee.cost()}\n")

    # Coffee with Milk and Sugar
    coffee_with_milk_and_sugar = Sugar(Milk(coffee))
    print(f"Order: {coffee_with_milk_and_sugar.description()}")
    print(f"Cost: ₹{coffee_with_milk_and_sugar.cost()}\n")

    # Coffee with Milk, Sugar, and Caramel
    fancy_coffee = Caramel(Sugar(Milk(coffee)))
    print(f"Order: {fancy_coffee.description()}")
    print(f"Cost: ₹{fancy_coffee.cost()}\n")
