# Getter: A method that allows you to access an attribute in a given class
# @property

# Setter: A method that allows you to set or mutate the value of an attribute in a class
# @setter

# The setter method automatically handles the creation of self._name when you assign a value to self.name. Here's how it works:

# When you write self.name = name in the constructor, you're not directly assigning to self._name. Instead, Python triggers the setter method @name.setter.
# Inside the setter, the condition if isinstance(value, str): checks whether the value you're assigning is a valid string. If it is, the setter creates and assigns the value to self._name.
# So, the creation and assignment of self._name happens automatically within the setter method whenever you try to assign a value to self.name.
class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age  # Public attribute

    # Getter for 'name'
    @property
    def name(self):
        print("Getting name")
        return self._name

    # Setter for 'name'
    @name.setter
    def name(self, value):
        print("Setting name")
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string.")

    # Getter for 'age'
    @property
    def age(self):
        print("Getting age")
        return self._age

    # Setter for 'age'
    @age.setter
    def age(self, value):
        print("Setting age")
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive number.")


# Example usage
person = Person("John", 25)

# Accessing the public attribute through getter
print(person.name)  # Output: John (with "Getting name" printed)

# Setting the public attribute through setter
person.name = "Jane"  # Output: Setting name

# Accessing the public attribute after modification
print(person.name)  # Output: Jane (with "Getting name" printed)


# Use self.name = name (i.e., the property) if you want to enforce validation or processing every time the attribute is set.

# Use self._name = name if you want to bypass the setter and directly assign the value,
# but this should typically only be done internally within the class if you are sure you don't need validation.


# __________________________________________________________________________________________________________________

#
# In Python, when you assign a value to an attribute like self.name = name inside the __init__ method, it behaves differently if you have defined a setter for that attribute using the @property decorator. Here's a step-by-step explanation of how this works in your case:
#
# 1. Attribute Assignment in __init__
# When the __init__ method is called, it contains:
#
# python
# Copy code
# self.name = name
# At first glance, it looks like this directly assigns the value of name to the self.name attribute. However, since self.name is decorated with @property, Python does not directly assign the value to self.name. Instead, it triggers the setter method for name.
#
# 2. How the Setter is Triggered
# When you define a @property and a corresponding setter, like this:
#
# python
# Copy code
# @property
# def name(self):
#     return self._name
#
# @name.setter
# def name(self, value):
#     if isinstance(value, str):
#         self._name = value
#     else:
#         raise ValueError("Name must be a string.")
# The line self.name = name in __init__ translates into a call to the setter method instead of directly setting the attribute. This is because the name attribute is managed through the property mechanism.
#
# 3. Setter in Action
# When self.name = name is executed in __init__, Python internally does something like this:
#
# python
# Copy code
# self.name("John")  # Triggers the setter for name
# This means it calls the @name.setter method with the argument "John". The setter method is executed as follows:
#
# python
# Copy code
# @name.setter
# def name(self, value):
#     if isinstance(value, str):
#         self._name = value  # Assigns the validated value to the private attribute _name
#     else:
#         raise ValueError("Name must be a string.")
# In this case:
#
# The setter checks if value (which is "John") is a string.
# Since "John" is a string, the setter assigns it to the private attribute self._name.
# 4. Why Use the Setter?
# The setter allows you to add logic (like validation or transformation) before actually setting the value of the attribute. In this case:
#
# The setter checks if the value is a string before assigning it to self._name.
# If it were not a string, it would raise a ValueError, ensuring that invalid data is not assigned.
# 5. Private Attribute self._name
# The actual value "John" is stored in a private attribute called self._name. The underscore convention (_name) indicates that this attribute is intended to be private and should not be accessed directly outside the class.
#
# By using the @property decorator and setter method, you control how the name attribute is accessed and modified, while storing the data in self._name.
