from math import sqrt, pow

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
        a, b, c, *_ = args
        cls._check_trg(a, b, c)
        return super(Triangle, cls).__new__(cls)

    def __init__(
        self,
        a: int | float,
        b: int | float,
        c: int | float,
        *_,
    ) -> None:
        self.__a, self.__b, self.__c = a, b, c
        self.__hipotenusa, self.__side_1, self.__side_2 = sorted(
            [a, b, c],
            reverse=True,
        )

    def __str__(self) -> str:
        return f"{self.__hipotenusa=} {self.__side_1=} {self.__side_2=}"

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

    @staticmethod
    def _check_trg(*args: tuple[int | float]) -> None:
        if False in [isinstance(i, (int, float)) for i in args]:
            raise TypeError("The sides must be int or float!")

        if False in [i > 0 for i in args]:
            raise ValueError("The sides cannot be less than 0!")

        a, b, c = args
        if not ((a + b > c) & (a + c > b) & (b + c > a)):
            raise Exception(f"Two sides cannot be less than a third! {args}")

    @property
    def a(self) -> int | float:
        return self.__a

    @property
    def b(self) -> int | float:
        return self.__b

    @property
    def c(self) -> int | float:
        return self.__c
