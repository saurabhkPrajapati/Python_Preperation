# Target (CustomLogger): Represents the interface used by your application.
# Adaptee (python_logger): Python's logging library, which has a different interface.
# Adapter (LoggingAdapter): Bridges the gap by converting log_message() calls into appropriate calls to the logging library methods like info() or error().

# Reusability: You can integrate the logging library into your application without modifying the existing code.
# Flexibility: If you decide to switch to a different logging system, you only need to update the adapter.
# Compatibility: Maintains the existing interface while leveraging the power of a new system


import logging


# Target interface: CustomLogger
class CustomLogger:
    def log_message(self, level, message):
        """Logs a message with a specific level."""
        raise NotImplementedError("Subclasses must implement this method.")


# Adaptee: Python's logging library with an incompatible interface
logging.basicConfig(level=logging.INFO)
python_logger = logging.getLogger("AppLogger")


# Adapter: Converts CustomLogger to work with Python's logging library
class LoggingAdapter(CustomLogger):
    def __init__(self, adaptee):
        self.python_logger = adaptee  # Python's logging library

    def log_message(self, level, message):
        """Adapts the log_message method to the logging library interface."""
        if level == "info":
            self.python_logger.info(message)
        elif level == "error":
            self.python_logger.error(message)
        elif level == "debug":
            self.python_logger.debug(message)
        else:
            self.python_logger.warning(f"Unknown level '{level}': {message}")


# Client code
def use_logger(logger):
    """Uses the logger through the CustomLogger interface."""
    logger.log_message("info", "This is an info message.")
    logger.log_message("debug", "This is a debug message.")
    logger.log_message("error", "This is an error message.")
    logger.log_message("unknown", "This is a message with an unknown level.")


# Create the adapter to connect the CustomLogger interface with Python's logging library
adapter = LoggingAdapter(python_logger)

# Using the adapter
adapter.log_message("info", "Adapter in action!")

# Client code can now use the logger through the CustomLogger interface
use_logger(adapter)

# Output:
# INFO:AppLogger:Adapter in action!
# INFO:AppLogger:This is an info message.
# WARNING:AppLogger:Unknown level 'debug': This is a debug message.
# ERROR:AppLogger:This is an error message.
# WARNING:AppLogger:Unknown level 'unknown': This is a message with an unknown level.
