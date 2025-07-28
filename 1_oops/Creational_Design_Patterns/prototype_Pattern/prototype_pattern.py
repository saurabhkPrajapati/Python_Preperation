import copy


# Define the Prototype Product
class Car:
    def __init__(self, model, color, features):
        self.model = model
        self.color = color
        self.features = features  # List of features

    def add_feature(self, feature):
        self.features.append(feature)

    def __str__(self):
        return f"Car(model={self.model}, color={self.color}, features={self.features})"

    # Clone method to create a copy of the current object
    def clone(self):
        return copy.deepcopy(self)  # Deep copy to ensure nested objects are cloned


# Usage of the Prototype pattern
original_car = Car("Sedan", "Red", ["Air Conditioning", "Navigation System"])
print("Original Car:", original_car)

# Clone the original car to create a new car with some changes
cloned_car = original_car.clone()
cloned_car.color = "Blue"  # Change color of cloned car
cloned_car.add_feature("Sunroof")  # Add new feature to cloned car

print("Cloned Car:", cloned_car)
print("Original Car after cloning:", original_car)  # Original remains unchanged
