from geometry import Triangle

__all__ = [
    "Pyramid",
]


class Pyramid(Triangle):
    """
    Pyramid object:
    metods: size_v, get_h, set_h
    """
    def __new__(cls, *args):
        *_, h = args
        if not isinstance(h, (int, float)):
            raise TypeError("The h must be int or float!")
        return super(Pyramid, cls).__new__(cls, *args)

    def __init__(
        self, a: int | float, b: int | float, c: int | float, h: int | float
    ) -> None:
        super().__init__(a, b, c)
        self.__h = h

    def h_get(self) -> int | float:
        return self.__h

    def h_set(self, value) -> int | float:
        if isinstance(value, (int, float)):
            self.__h = value
        print("The sides must be int or float!")

    @property
    def size_v(self) -> float:
        return abs((self.get_area * self.__h) / 3)

    h = property(h_get, h_set)
