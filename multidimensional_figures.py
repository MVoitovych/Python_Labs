from abc import abstractmethod
from abstract_geometric_figure import AbstractGeometricFigure


class TwoDimensional(AbstractGeometricFigure):
    def __init__(self):
        super().__init__(2)

    @abstractmethod
    def get_area(self) -> float:
        ...

    def print_info(self) -> None:
        print(f"{self.__class__.__name__} with {self.get_area():.2f} area ")


class ThreeDimensional(AbstractGeometricFigure):
    def __init__(self):
        super().__init__(3)

    @abstractmethod
    def get_side_area(self) -> float:
        ...

    @abstractmethod
    def get_volume(self) -> float:
        ...

    def print_info(self):
        print(f"{self.__class__.__name__} with {self.get_side_area():.2f} side area and {self.get_volume():.2f} volume")
