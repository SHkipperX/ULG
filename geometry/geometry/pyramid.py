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
            raise TypeError("The height must be int or float!")

        if not (h > 0):
            raise ValueError("The height cannot be less than 0!")

        return super(Pyramid, cls).__new__(cls, *args)

    def __init__(
        self,
        a: int | float,
        b: int | float,
        c: int | float,
        h: int | float,
    ) -> None:
        super(Pyramid, self).__init__(a, b, c)
        self.__heigth = h

    def __str__(self) -> str:
        sides = super().__str__()
        return f"{sides} {self.__heigth=}"

    @property
    def h(self) -> int | float:
        return self.__heigth

    @h.setter
    def h(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("The height must be int or float!")
        if not (value > 0):
            raise ValueError("The height cannot be less than 0!")
        self.__heigth = value

    @property
    def size_v(self) -> float:
        return (self.get_area * self.__heigth) / 3
