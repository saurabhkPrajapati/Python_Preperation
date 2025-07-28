# Static methods don’t have access to the class or instance (no cls or self), so they are less suitable for factory methods,
# because they cannot easily instantiate or return objects of the class or its subclasses.

# Class methods, on the other hand, have access to the class (cls)
# and are designed for such scenarios where you might want to return different instances based on class-level logic.

# Using a @staticmethod/classmethod as a factory method in Python is a great way to create alternative constructors for a class

# Using @classmethod here provides flexibility, allowing factory_method to return instances of whichever class calls it,
# making it ideal for factory methods in inheritance hierarchies.


class Vehicle:
    brand_name = 'BMW'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):  # cannot use static method here
        # ind_price = dollar * 76
        # create new Vehicle object
        return cls(name, (price * 75))
        # return Person(name, (price * 75))

    def show(self):
        print(self.name, self.price)
        self.brand_name = 123214
        print(Vehicle.brand_name, self.brand_name)


class Car(Vehicle):
    def __init__(self, name, price):
        super().__init__(name, price)

    @staticmethod
    def average(name, distance, fuel_used):
        mileage = distance / fuel_used
        print(name, 'Mileage', mileage, sep=".....")


bmw_us = Car('BMW X5', 65000)
bmw_us.show()

# class method of parent class is available to child class
# this will return the object of calling class
bmw_ind = Car.from_price('BMW X6', 65000)
bmw_ind.show()
bmw_ind.average('BMW X5', 65000, 30)
# check type
print(type(bmw_ind))
