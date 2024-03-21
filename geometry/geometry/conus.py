from geometry import Circle

__all__ = [
    "Conus",
]


class Conus(Circle):
    """Conus"""

    def __new__(cls, radius, h):
        instance = super(Conus, cls).__new__(cls, radius)
        return instance

    def __init__(self, radius: int | float, h: int | float) -> None:
        super().__init__(radius)
        self.__h = h

    @property
    def size_v(self) -> float:
        return (1 / 3) * self.get_area * self.h

    def h_get(self) -> int | float:
        return self.__h

    def h_set(self, value) -> int | float:
        if isinstance(value, (int, float)):
            self.__h = value
            return
        print("The sides must be int or float!")

    h = property(h_get, h_set)
