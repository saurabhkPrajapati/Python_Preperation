def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Singleton:
    def __init__(self, value=None):
        self.value = value


# Usage
singleton1 = Singleton(10)
print(singleton1.value)  # Output: 10

singleton2 = Singleton(20)
print(singleton2.value)  # Output: 10 (still the same instance)

print(singleton1 is singleton2)  # Output: True (both are the same instance)
