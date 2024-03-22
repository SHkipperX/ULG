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
        self.__height = h

    @property
    def height(self) -> int | float:
        """
        returns the height of the pyramide
        """
        return self.__height

    @height.setter
    def height(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("The height must be int or float!")
        if not (value > 0):
            raise ValueError("The height cannot be less than 0!")
        self.__height = value

    @property
    def size_v(self) -> float:
        """
        returns the volume of the pyramide
        """
        return (self.get_area * self.__height) / 3

    def __str__(self) -> str:
        sides = super().__str__()
        return f"{sides} {self.__height=}"

    def __repr__(self) -> str:
        trg_repr = super().__repr__()
        edit = trg_repr.replace(")", f", {self.__height!r})")
        return edit
