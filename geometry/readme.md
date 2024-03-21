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
    print(triangle.get_type_triangle)
    > 1.7623563771269384
    > obtuse angled

### you can also create your own class. For example, a cone (just don't forget to redefine the __new__ method)


# update #
1.1) add Pyramid, Conus in gemetry module