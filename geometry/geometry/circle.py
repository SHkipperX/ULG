from math import pi, pow
import re

__all__ = [
    "Circle",
]


class Circle:
    """
    Circle object.
    You can extend this model.
    The default methods are get_area.
    """

    def __new__(cls, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("The radius must be a int or float!")

        if not (radius > 0):
            raise ValueError("The radius must be greater than 0!")

        return super(Circle, cls).__new__(cls)

    def __init__(
        self,
        radius: int | float,
    ) -> None:
        self.__radius = radius

    @property
    def get_area(self) -> float:
        return pi * pow(self.__radius, 2)

    def get_r(self) -> int | float:
        return self.__radius

    def set_r(self, value: int | float) -> None:
        if isinstance(value, (int, float)):
            if value > 0:
                self.__radius = value
                return
            raise ValueError("The radius must be greater than 0!")
        raise TypeError("The radius must be a int or float!")

    r = property(get_r, set_r)
