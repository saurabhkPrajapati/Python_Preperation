class Singleton(object):
    """
    Singleton_Pattern pattern implementation using a decorator.
    This approach allows decorating existing classes to make them singletons.
    """

    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        """
        This method is called when the Singleton_Pattern object is used like a function
        (e.g., singleton_object = Singleton_Pattern(MyClass)()).
        If an instance doesn't exist, it creates one and returns it.
        Otherwise, it returns the existing instance.
        """
        if not self._instance:
            self._instance = self._cls(*args, **kwargs)
        return self._instance


# Usage
@Singleton
class Logger:
    """
    Example class representing a logger.
    """

    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        # Write message to the log file
        print(f"Logging to {self.log_file}: {message}")


# Create a single instance of the Logger
singleton_logger = Logger("app.log")

# Call the log method on the same instance
singleton_logger.log("This is a message from the singleton logger.")
singleton_logger2 = Logger("another_file.log")  # This won't create a new instance

# Check object identity to verify it's the same instance
if singleton_logger is singleton_logger2:
    print("Singleton_Pattern works! Both objects are the same instance.")
