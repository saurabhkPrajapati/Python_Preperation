class Circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def __str__(self):
        return f"{self.color}, {self.radius}"


class Square:
    def __init__(self, color, side_length):
        self.color = color
        self.side_length = side_length

    def __str__(self):
        return f"{self.color}, {self.side_length}"

    def check(self):
        print(self.color)


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def __str__(self):
        return f"{self.length}, {self.breadth}"

    def check(self):
        print(self.length)


class ColoredCircle(Circle, Square, Rectangle):
    def __init__(self, color, radius, side_length, length, breadth):
        super().__init__(color, radius)  # Use super() to call Circle's constructor
        # Circle.__init__(self, color, radius)  # Use super() to call Circle's constructor
        Square.__init__(self, color, side_length)  # Use Square to call Square's constructor
        Rectangle.__init__(self, length, breadth)  # Use Rectangle to call Rectangle's constructor
        super().check()

    def __str__(self):
        return f"{self.color}, {self.radius}, {self.side_length}, {self.length}, {self.breadth}"


# Example usage
print(ColoredCircle('black', 2, 4, 5, 6), end="\n\n")
print(Square('black', 2), end="\n\n")
print(Circle('black', 2), end="\n\n")

