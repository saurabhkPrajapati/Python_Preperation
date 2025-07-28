import threading


def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def get_instance(*args, **kwargs):
        with lock:  # Ensure thread safety
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

    return get_instance


@singleton
class Example:
    def __init__(self, value):
        self.value = value


# Usage
obj1 = Example(10)
obj2 = Example(20)

print(obj1 is obj2)  # Output: True
print(obj1.value)  # Output: 10
print(obj2.value)  # Output: 10
