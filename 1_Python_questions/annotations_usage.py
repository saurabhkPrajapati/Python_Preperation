from typing import List, Dict


# Function annotation example
def greet(name: str) -> str:
    return f"Hello, {name}!"


# Class annotation example
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


# Function with annotations for parameters and return value
def process_data(data: List[int]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for num in data:
        if num % 2 == 0:
            result[f"even_{num}"] = num
        else:
            result[f"odd_{num}"] = num
    return result


# Using annotations for variables
x: int = 10
y: float = 3.14
z: str = "Hello"


# Using annotations with default values
def add(x: int = 0, y: int = 0) -> int:
    return x + y


# Type hinting for complex data structures
# data: List[Dict[str, Union[int, str]]]
def process_data2(data: List[Dict[str, int]]) -> List[int]:
    return [sum(d.values()) for d in data]


# Type hinting for variables with Union
from typing import Union


def display_value(value: Union[int, str]) -> None:
    print(f"The value is: {value}")


# Using annotations for class attributes
class MyClass:
    attr1: int
    attr2: str

    def __init__(self, attr1: int, attr2: str) -> None:
        self.attr1 = attr1
        self.attr2 = attr2
