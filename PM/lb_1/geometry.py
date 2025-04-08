class Geom_obj:
    pass

class Dot(Geom_obj):
    pass

class Straight(Geom_obj):
    pass

class Flat_figure(Geom_obj):
    pass

class Ray(Dot):
    pass

class segment(Dot, Straight):
    pass

class Polygon(Dot, Flat_figure):
    pass

class Rectangle(Polygon):
    pass

class Square(Rectangle):
    pass