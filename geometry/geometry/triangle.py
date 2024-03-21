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
        if len(args) != 3:
            raise ValueError("The number of sides cannot exceed 3!")

        if False in [isinstance(i, (int, float)) for i in args]:
            raise TypeError("The sides cannot  or be a string!")
        
        if False in [i > 0 for i in args]:
            raise ValueError("The sides cannot be less than 0!")
        
        a, b, c = args
        if not ((a + b > c) & (a + c > b) & (b + c > a)):
            raise Exception(f"Two sides cannot be less than a third! {args}")
        return super(Triangle, cls).__new__(cls)

    def __init__(
        self,
        a: int | float,
        b: int | float,
        c: int | float,
    ) -> None:
        self.a, self.b, self.c = a, b, c
        self.__hipotenusa, self.__side_1, self.__side_2 = sorted(
            [a, b, c],
            reverse=True,
        )
    @property
    def get_area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def get_type_triangle(self) -> str:
        
        if pow(self.__side_1, 2) + pow(self.__side_2, 2) < pow(self.__hipotenusa, 2):
            return "obtuse angled"

        if pow(self.__side_1, 2) + pow(self.__side_2, 2) > pow(self.__hipotenusa, 2):
            return "acute angled"

        return "rectangular"