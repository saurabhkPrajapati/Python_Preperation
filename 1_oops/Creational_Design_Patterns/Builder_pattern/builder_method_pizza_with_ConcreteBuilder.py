from abc import ABC, abstractmethod


# Define the Product
class Pizza:
    def __init__(self):
        self.size = None
        self.crust_type = None
        self.toppings = []
        self.sauce = None

    def __str__(self):
        return (f"Pizza(size={self.size}, crust_type={self.crust_type}, "
                f"toppings={self.toppings}, sauce={self.sauce})")


# Define the Abstract Builder_pattern
class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()  # Initialize a fresh Pizza object

    @abstractmethod
    def set_size(self):
        pass

    @abstractmethod
    def set_crust(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass

    @abstractmethod
    def set_sauce(self):
        pass

    def build(self):
        return self.pizza  # Return the constructed Pizza


# Concrete Builder_pattern for Margherita Pizza
class MargheritaPizzaBuilder(PizzaBuilder):

    def set_size(self):
        self.pizza.size = "Medium"
        return self

    def set_crust(self):
        self.pizza.crust_type = "Thin Crust"
        return self

    def add_topping(self):
        self.pizza.toppings.append("Basil")
        return self

    def set_sauce(self):
        self.pizza.sauce = "Tomato"
        return self


# Concrete Builder_pattern for Pepperoni Pizza
class PepperoniPizzaBuilder(PizzaBuilder):

    def set_size(self):
        self.pizza.size = "Large"
        return self

    def set_crust(self):
        self.pizza.crust_type = "Thick Crust"
        return self

    def add_topping(self):
        self.pizza.toppings.append("Pepperoni")
        self.pizza.toppings.append("Mozzarella")
        return self

    def set_sauce(self):
        self.pizza.sauce = "Marinara"
        return self


class PizzaDirector:
    def __init__(self, builder):
        self.final_pizza = self.construct_pizza(builder)

    def construct_pizza(self, builder):
        return (
            builder.set_size()
            .set_crust()
            .add_topping()
            .set_sauce().
            build()
        )


margherita_builder = MargheritaPizzaBuilder()
director = PizzaDirector(margherita_builder)
print(director.final_pizza)

pepperoni_builder = PepperoniPizzaBuilder()
director = PizzaDirector(margherita_builder)
print(director.final_pizza)
