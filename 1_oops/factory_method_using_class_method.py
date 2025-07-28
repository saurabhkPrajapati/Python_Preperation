class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_name(cls, name):
        return cls(name)


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Golden Retriever"


# Using class method as a factory method
dog = Dog.from_name("Buddy")
print(type(dog))  # Outputs: <class '__main__.Dog'>
print(dog.name)  # Outputs: Buddy
print(dog.breed)  # Outputs: Golden Retriever


# ____________________________________________________________________________________________________________________


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def create(cls, name, price, discount_percent=None):
        if discount_percent is not None:
            return DiscountedProduct(name, price, discount_percent)
        return cls(name, price)  # Notice the use of `cls` here

    def display(self):
        print(f"Product Name: {self.name}, Price: ${self.price:.2f}")


class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        discounted_price = price - (price * discount_percent / 100)
        super().__init__(name, discounted_price)
        self.discount_percent = discount_percent

    def display(self):
        print(f"Discounted Product Name: {self.name}, Discounted Price: ${self.price:.2f}")


# Usage
product = Product.create("Regular Product", 100)
discounted_product = Product.create("Discounted Product", 100, discount_percent=20)

product.display()  # Output: Product Name: Regular Product, Price: $100.00
discounted_product.display()  # Output: Discounted Product Name: Discounted Product, Discounted Price: $80.00

test = DiscountedProduct.create("Discounted Product", 100),  # This should give error
