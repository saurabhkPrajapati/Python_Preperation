def decorator_func(func):
    def wrapper_func(*args, **kwargs):
        print(f'there are {len(args)} positional arguments and {len(kwargs)} keyword arguments')
        return func(*args, **kwargs)

    return wrapper_func


@decorator_func
def names_and_age(year1, year2, name1='Joe', name2='Harry'):
    return f'{name1} was released in {year1} and {name2} was released in {year2}'


print(names_and_age(1997, 1986, name1="Titanic", name2="Top Gun"))


####################################################################
# first decorator will be called first
# then second decorator will be called


# First decorator
def first_decorator(func):
    def wrapper(*args, **kwargs):
        print("First Decorator: Something before the function is called.")
        result = func(*args, **kwargs)
        print("First Decorator: Something after the function is called.")
        return result

    return wrapper


# Second decorator
def second_decorator(func):
    def wrapper(*args, **kwargs):
        print("Second Decorator: Something else before the function is called.")
        result = func(*args, **kwargs)
        print("Second Decorator: Something else after the function is called.")
        return result

    return wrapper


# Applying nested decorators
@first_decorator
@second_decorator
def my_function():
    print("My function is called.")


# Call the decorated function
my_function()


# __________________________________________________________________________________________________________________________

def check_even(func):
    def wrapper(arg):
        if arg % 2 != 0:
            raise ValueError(f"The argument {arg} is not even.")
        return func(arg)

    return wrapper


def double_arg(func):
    def wrapper(arg):
        return func(arg * 2)

    return wrapper


@check_even
@double_arg
def process_number(number):
    return f"Processed number: {number}"


# Example usage
try:
    result = process_number(4)  # This will double the argument to 8 and then check if it's even
    print(result)  # Output: Processed number: 8
except ValueError as e:
    print(e)

try:
    result = process_number(3)  # This will double the argument to 6 and then check if it's even
    print(result)  # Output: Processed number: 6
except ValueError as e:
    print(e)  # Output: The argument 3 is not even.


# _______________________________________________________________________________________________________

# TypeError: 'tuple' object does not support item assignment, occurs because args is a tuple, and tuples in Python are immutable.
# Use this:      args_list = list(args)

def check_even(func):
    def wrapper(*args, **kwargs):
        args_list = list(args)
        if args_list[0] % 2 != 0:
            raise ValueError("Not Div")
        return func(*args_list)

    return wrapper


def double_arg(func):
    def wrapper(*args, **kwargs):
        args_list = list(args)
        args_list[0] = args_list[0] * 2
        return func(*args)

    return wrapper


@check_even
@double_arg
def process_number(number):
    return [f"Processed number: {number}"]


# Example usage
try:
    result = process_number(4)  # This will double the arguments to 8 and 12
    print(result)

    result = process_number(3)  # This will raise a ValueError
    print(result)
except ValueError as e:
    print(e)
