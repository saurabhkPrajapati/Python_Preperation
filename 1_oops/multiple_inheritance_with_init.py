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


class ColoredCircle(Circle, Square):
    def __init__(self, color, radius, side_length):
        super().__init__(color, radius)  # Call Circle's constructor
        # Circle.__init__(self, color, radius)  # Call Circle's constructor
        Square.__init__(self, color, side_length)  # Call Square's constructor

    def __str__(self):
        return f"{self.color}, {self.radius}, {self.side_length}"


print(ColoredCircle('black', 2, 4))
