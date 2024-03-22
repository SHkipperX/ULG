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

    def __init__(self, radius: int | float, height: int | float) -> None:
        super(Conus, self).__init__(radius)
        self.__heigth = height

    @property
    def size_v(self) -> float:
        """
        returns the volume of the cone
        """
        return (1 / 3) * self.get_area * self.height

    @property
    def height(self) -> int | float:
        """
        returns the height of the cone
        """
        return self.__heigth

    @height.setter
    def height(self, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("The height must be int or float!")
        if not (value > 0):
            raise ValueError("The height must be greater than 0!")
        self.__heigth = value

    def __str__(self) -> str:
        radius = super().__str__()
        return f"{radius} {self.__heigth=}"

    def __repr__(self) -> str:
        cre_repr = super().__repr__()
        edit = cre_repr.replace(")", f", {self.__heigth!r}")
        return edit
