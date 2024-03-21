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
            raise TypeError("The radius must be a int or float!")
        
        if not (radius > 0):
            raise ValueError("The radius must be greater than 0!")
        
        return super(Circle, cls).__new__(cls)
    def __init__(
        self,
        radius: int | float,
    ) -> None:
        self.radius = radius

    @property
    def get_area(self) -> float:
        return pi * pow(self.radius, 2)
