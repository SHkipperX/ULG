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
        if len(args) < 3:
            raise Exception(
                f"lenght {args=} must be greater (if u inheritance) than or equal to 3"
            )
        a, b, c, *_ = args
        cls._check_trg(a, b, c)
        return super(Triangle, cls).__new__(cls)

    def __init__(
        self,
        a: int | float,
        b: int | float,
        c: int | float,
    ) -> None:
        self.__hipotenusa, self.__side_1, self.__side_2 = sorted(
            [a, b, c],
            reverse=True,
        )

    @property
    def get_area(self) -> float:
        """
        returns the area of the base
        """
        p = (self.__hipotenusa + self.__side_1 + self.__side_2) / 2
        return sqrt(
            p * (p - self.__hipotenusa) * (p - self.__side_1) * (p - self.__side_2)
        )

    @property
    def get_type_triangle(self) -> str:
        """
        returns the type of the base triangle
        """
        if pow(self.__side_1, 2) + pow(self.__side_2, 2) < pow(self.__hipotenusa, 2):
            return "obtuse angled"

        if pow(self.__side_1, 2) + pow(self.__side_2, 2) > pow(self.__hipotenusa, 2):
            return "acute angled"

        return "rectangular"

    @staticmethod
    def _check_trg(*args) -> None:
        if False in [isinstance(i, (int, float)) for i in args]:
            raise TypeError("The sides must be int or float!")

        if False in [i > 0 for i in args]:
            raise ValueError("The sides cannot be less than 0!")

        a, b, c, *_ = args
        if not ((a + b > c) & (a + c > b) & (b + c > a)):
            raise Exception(f"Two sides cannot be less than a third! {args}")

    @property
    def hipotenusa(self) -> int | float:
        """
        returns the hypotenuse of the base
        """
        return self.__hipotenusa

    @property
    def side_1(self) -> int | float:
        """
        returns the middle side
        """
        return self.__side_1

    @property
    def side_2(self) -> int | float:
        """
        returns the smallest side
        """
        return self.__side_2

    def __str__(self) -> str:
        return f"{self.__hipotenusa=} {self.__side_1=} {self.__side_2=}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__hipotenusa!r}, {self.__side_1!r}, {self.__side_2!r})"
