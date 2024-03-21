# Ultra lite Geometry - ULG #

# U can import two module from geometry
## import classes
    from geometry import Triangle, Circle
## create an instance of the class
    circle = Circle(2)
    triangle = Trianle(2.2, 3, 5)

## call the method
    print(circle.get_area)
    > 12.566370614359172

    print(triangle.get_area)
    print(triangle)
    > 1.7623563771269384
    > obtuse angled

### you can also create your own class. For example, a cone (just don't forget to redefine the __new__ method)
    class Conus(Circle):
        def __new__(cls, radius, h):
            instance = super(Conus, cls).__new__(cls, radius)
            return instance
        
        def __init__(self, radius: int | float, h: int | float) -> None:
            super().__init__(radius)
            self.h = h
        
        @property
        def V(self) -> float:
            return (2/3) * self.get_area * self.h

        a = Conus(2, 3)
        print(a.V)    
    > 25.132741228718345
