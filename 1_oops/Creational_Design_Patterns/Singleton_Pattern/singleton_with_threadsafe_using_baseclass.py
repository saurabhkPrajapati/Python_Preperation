import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # Check if an instance already exists
            with cls._lock:  # Acquire the lock
                if not cls._instance:  # Double-check to avoid race condition
                    cls._instance = super(Singleton, cls).__new__(cls)  # Create a new instance
        return cls._instance  # Return the existing instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Check if the instance is already initialized
            self.value = value
            self.initialized = True  # Mark as initialized


# Usage
def create_singleton(value):
    singleton = Singleton(value)
    print(f'Singleton value: {singleton.value}')


# Create multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=create_singleton, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

# Verify that all threads refer to the same instance
singleton1 = Singleton(10)
singleton2 = Singleton(20)
print(singleton1 is singleton2)  # Output: True (both are the same instance)
