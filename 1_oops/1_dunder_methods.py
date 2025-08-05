class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector with x={self.x}, y={self.y}"


# Usage
v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)  # Uses __add__: Output is Vector(7, 10)
print(v1 == v2)  # Uses __eq__: Output is False
print(str(v1))  # Uses __str__: Output is Vector with x=2, y=3
