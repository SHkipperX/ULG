from math import pi, pow

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
            raise TypeError("The radius must be int or float!")
        if not (radius > 0):
            raise ValueError("The radius cannot be less than 0!")
        return super(Circle, cls).__new__(cls)

    def __init__(
        self,
        radius: int | float,
    ) -> None:
        self.__radius = radius

    @property
    def get_area(self) -> float:
        return pi * pow(self.__radius, 2)

    @property
    def r(self) -> int | float:
        return self.__radius

    @r.setter
    def r(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("The radius must be int or float!")
        if not (value > 0):
            raise ValueError("The radius cannot be less than 0!")
        self.__radius = value
