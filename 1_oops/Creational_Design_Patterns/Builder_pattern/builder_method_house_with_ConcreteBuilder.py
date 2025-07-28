from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
        self.interior = None

    def __str__(self):
        return (f"House with {self.foundation} foundation, "
                f"{self.walls} walls, {self.roof} roof, and a {self.interior} interior.")


# Define the Builder_pattern Interface (HouseBuilder)


class HouseBuilder(ABC):
    def __init__(self):
        self.house = House()

    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def build_interior(self):
        pass

    def get_house(self):
        return self.house


# Define Concrete Builders for Each Type of House
class WoodenHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "wooden piles"
        return self

    def build_walls(self):
        self.house.walls = "wooden planks"
        return self

    def build_roof(self):
        self.house.roof = "wooden shingles"
        return self

    def build_interior(self):
        self.house.interior = "rustic wooden interior"
        return self


# Define Concrete Builders for Each Type of House
class GlassHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "concrete with steel beams"
        return self

    def build_walls(self):
        self.house.walls = "glass panels"
        return self

    def build_roof(self):
        self.house.roof = "glass roof"
        return self

    def build_interior(self):
        self.house.interior = "modern minimalist interior"
        return self


# Define Concrete Builders for Each Type of House
class StoneHouseBuilder(HouseBuilder):
    def build_foundation(self):
        self.house.foundation = "stone slabs"
        return self

    def build_walls(self):
        self.house.walls = "stone bricks"
        return self

    def build_roof(self):
        self.house.roof = "slate tiles"
        return self

    def build_interior(self):
        self.house.interior = "traditional stone interior"
        return self


# Define the Director (Optional)

# The Director class orchestrates the building process, ensuring that the construction steps are executed in a specific order.
# This step is optional and useful if you want to standardize the construction sequence.


class HouseDirector:
    def __init__(self, builder):
        self.house = self.construct_house(builder)

    def construct_house(self, builder):
        return (
            builder.build_foundation()
            .build_walls()
            .build_roof()
            .build_interior()
            .get_house()
        )


# Construct a wooden house
wooden_builder = WoodenHouseBuilder()
director = HouseDirector(wooden_builder)
print(director.house)

# Direct way
wooden_builder = WoodenHouseBuilder()
wooden_house2 = (wooden_builder.build_foundation()
                 .build_walls()
                 .build_roof()
                 .build_interior()
                 .get_house())
print(wooden_house2)


class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        return (self.builder.build_foundation()
                .build_walls()
                .build_roof()
                .build_interior()
                .get_house())


# Construct a wooden house
wooden_builder = WoodenHouseBuilder()
director = HouseDirector(wooden_builder)
wooden_house = director.construct_house()
print(wooden_house)
# Output: House with wooden piles foundation, wooden planks walls, wooden shingles roof, and a rustic wooden interior.

# Construct a glass house
glass_builder = GlassHouseBuilder()
director = HouseDirector(glass_builder)
glass_house = director.construct_house()
print(glass_house)
# Output: House with concrete with steel beams foundation, glass panels walls, glass roof, and a modern minimalist interior.

# Construct a stone house
stone_builder = StoneHouseBuilder()
director = HouseDirector(stone_builder)
stone_house = director.construct_house()
print(stone_house)
# Output: House with stone slabs foundation, stone bricks walls, slate tiles roof, and a traditional stone interior.
