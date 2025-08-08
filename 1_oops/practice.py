"""
super().__init__(**kwargs)	calls the next class in MRO, passing remaining keyword arguments
Enables multiple inheritance so all parent classes can initialize their own attributes
"""

class Circle:
    def __init__(self, radius=2, **kwargs):
        print("Circle init")
        super().__init__(**kwargs)
        self.radius = radius

class Square:
    def __init__(self, side_length=3, **kwargs):
        print("Square init")
        super().__init__(**kwargs)
        self.side_length = side_length

class ColoredCircle(Circle, Square):
    """Initialiazing colour inside ColoredCircle and removing form Circle and Square classes"""
    def __init__(self, color="Red", **kwargs):
        print("ColoredCircle init")
        super().__init__(**kwargs)
        self.color = color

    def __str__(self):
        return f"{self.color}, {self.radius}, {self.side_length}"

print(ColoredCircle(radius=5, side_length=10))