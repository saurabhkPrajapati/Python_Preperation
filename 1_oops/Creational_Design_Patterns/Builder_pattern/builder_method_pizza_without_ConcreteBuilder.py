# Define the product
class Pizza:
    def __init__(self):
        self.size = None
        self.crust_type = None
        self.toppings = []
        self.sauce = None

    def __str__(self):
        return (f"Pizza(size={self.size}, crust_type={self.crust_type}, "
                f"toppings={self.toppings}, sauce={self.sauce})")


# Define the builder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()  # Initialize a fresh Pizza object

    def set_size(self, size):
        self.pizza.size = size
        return self  # Allows chaining

    def set_crust(self, crust_type):
        self.pizza.crust_type = crust_type
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def build(self):
        return self.pizza  # Return the constructed Pizza


# Using the Builder_pattern to Create a Complex Object
# Create a new pizza with various configurations using the builder
builder = PizzaBuilder()
pizza = (
    builder.set_size("Large")
    .set_crust("Thin Crust")
    .add_topping("Pepperoni")
    .add_topping("Mushrooms")
    .set_sauce("Marinara")
    .build()
)

print(pizza)
# Output: Pizza(size=Large, crust_type=Thin Crust, toppings=['Pepperoni', 'Mushrooms'], sauce=Marinara)
