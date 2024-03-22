from geometry import Circle

__all__ = [
    "Conus",
]


class Conus(Circle):
    """Conus"""

    def __new__(cls, *args):
        *_, h = args
        if not isinstance(h, (int, float)):
            raise TypeError("The height must be int or float!")
        if not (h > 0):
            raise ValueError("The value must be greater than 0!")
        return super(Conus, cls).__new__(cls, *args)

    def __init__(self, radius: int | float, h: int | float) -> None:
        super(Conus, self).__init__(radius)
        self.__h = h

    @property
    def size_v(self) -> float:
        return (1 / 3) * self.get_area * self.h

    @property
    def h(self) -> int | float:
        return self.__h

    @h.setter
    def h(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("The height must be int or float!")
        if not (value > 0):
            raise ValueError("The height must be greater than 0!")
        self.__h = value
