class CustomException(Exception):
    """Custom exception class."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"CustomException: {self.message}"


def example_function(value):
    if value < 0:
        raise CustomException("Value should be non-negative.")


user_input = -5
try:
    example_function(user_input)
except CustomException as ce:
    print(ce)
except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# ______________________________________________________________________

class CustomException(Exception):
    pass


try:
    # Raise a custom exception
    raise CustomException("Custom exception occurred")
except Exception:
    print("Handling exception using 'except (Exception)':")
    # print(f"Caught exception: {type(e).__name__}")
except CustomException as e:
    print("This block won't be reached because 'except (Exception)' catches all exceptions, including subclasses")
