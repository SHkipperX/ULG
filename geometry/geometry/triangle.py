from math import sqrt, pow
from tabnanny import check
from typing import Any

__all__ = [
    "Triangle",
]


class Triangle:
    """
    Triangular object.
    You can extend this model.
    The default methods are get_area and get_type_triangle.
    """

    def __new__(cls, *args):
        cls.check_trg(*args)
        return super(Triangle, cls).__new__(cls)

    def __init__(
        self,
        a: int | float,
        b: int | float,
        c: int | float,
    ) -> None:
        self.__a, self.__b, self.__c = a, b, c
        self.__hipotenusa, self.__side_1, self.__side_2 = sorted(
            [a, b, c],
            reverse=True,
        )

    @property
    def get_area(self) -> float:
        p = (self.__a + self.__b + self.__c) / 2
        return sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

    @property
    def get_type_triangle(self) -> str:
        if pow(self.__side_1, 2) + pow(self.__side_2, 2) < pow(self.__hipotenusa, 2):
            return "obtuse angled"

        if pow(self.__side_1, 2) + pow(self.__side_2, 2) > pow(self.__hipotenusa, 2):
            return "acute angled"

        return "rectangular"

    @classmethod
    def check_trg(cls, *args):
        if len(args) != 3:
            raise ValueError("The number of sides cannot exceed 3!")

        if False in [isinstance(i, (int, float)) for i in args]:
            raise TypeError("The sides must be int or float!")

        if False in [i > 0 for i in args]:
            raise ValueError("The sides cannot be less than 0!")

        a, b, c = args
        if not ((a + b > c) & (a + c > b) & (b + c > a)):
            raise Exception(f"Two sides cannot be less than a third! {args}")
    
    def sorted_sides(self):
        self.__hipotenusa, self.__side_1, self.__side_2 = sorted(
            [self.__a, self.__b, self.__c],
            reverse=True,
        )

    def set_a(self, value):
        try:
            self.check_trg(value, self.__b, self.__c)
            self.__a = value
            self.sorted_sides()
        except Exception as _:
            print(_)

    def get_a(self):
        return self.__a

    def set_b(self, value):
        try:
            self.check_trg(self.__a, value, self.__c)
            self.__b = value
            self.sorted_sides()
        except Exception as _:
            print(_)

    def get_b(self):
        return self.__b

    def set_c(self, value):
        try:
            self.check_trg(self.__a, self.__b, value)
            self.__c = value
            self.sorted_sides()
        except Exception as _:
            print(_)

    def get_c(self):
        return self.__c

    a = property(get_a, set_a)
    b = property(get_b, set_b)
    c = property(get_c, set_c)
