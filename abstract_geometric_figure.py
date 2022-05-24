from abc import ABC, abstractmethod


class AbstractGeometricFigure(ABC):
    def __init__(self, dimensional):
        self.dimensional = dimensional

    @abstractmethod
    def print_info(self) -> None:
        ...
