def check_even(func):
    def wrapper(*args, **kwargs):
        args_list = args
        if args_list[0] % 2 != 0:
            raise ValueError("Not Div")
        return func(*args_list)

    return wrapper


def double_arg(func):
    def wrapper(*args, **kwargs):
        args_list = args
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
