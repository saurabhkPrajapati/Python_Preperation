class Singleton:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # Check if an instance already exists
            cls._instance = super(Singleton, cls).__new__(cls)  # Create a new instance
        return cls._instance  # Return the existing instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Check if the instance is already initialized
            self.value = value
            self.initialized = True  # Mark as initialized


# Usage
singleton1 = Singleton(10)
print(singleton1.value)  # Output: 10

singleton2 = Singleton(20)
print(singleton2.value)  # Output: 10 (still the same instance)

print(singleton1 is singleton2)  # Output: True (both are the same instance)
