from multidimensional_figures import *
from math import *


class Triangle(TwoDimensional):

    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return (self.base * self.height) / 2


class Circle(TwoDimensional):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius ** 2


class Cylinder(ThreeDimensional):

    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def get_volume(self) -> float:
        return pi * self.radius ** 2 * self.height

    def get_side_area(self) -> float:
        return 2 * pi * self.radius * self.height


class Cone(ThreeDimensional):
    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def get_volume(self) -> float:
        return pi * self.radius ** 2 * self.height / 3

    def get_side_area(self) -> float:
        return pi * self.radius * sqrt(self.radius ** 2 + self.height ** 2)


class Sphere(ThreeDimensional):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_volume(self) -> float:
        return pi * self.radius ** 3 * 4 / 3

    def get_side_area(self) -> float:
        return 4 * pi * self.radius ** 2
