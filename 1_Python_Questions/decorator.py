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
# take_first_four decorator will be called first
# then def sum_only_even decorator will be called


def take_first_four(func):
    def wrapper(*args, **kwargs):
        first_four = args[:4]  # Only first 4 positional arguments
        return func(*first_four, **kwargs)
    return wrapper


def sum_only_even(func):
    def wrapper(*args, **kwargs):
        even_numbers = [x for x in args if isinstance(x, int) and x % 2 == 0]
        return func(*even_numbers, **kwargs)
    return wrapper


@sum_only_even
@take_first_four
def add_numbers(*nums):
    return sum(nums)


# Test
print(add_numbers(1, 2, 3, 4, 5, 6, 8))  # 6 (2 + 4 from first four)
print(add_numbers(10, 12, 14, 15, 16))  # 36 (10 + 12 + 14 from first four)

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
