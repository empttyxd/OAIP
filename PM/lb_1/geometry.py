class Object:
    pass


class Point(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line(Object):
    def __init__(self, x1, x2, y1, y2):
        self.first = Point(x1, y1)
        self.second = Point(x2, y2)


class Flat_Shape(Object):
    pass


class Ray(Line, Point):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)


class Segment(Line, Point):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)


class Polygon(Point, Flat_Shape):
    def __init__(self, *args):
        Point.__init__(self, *args[0])
        self.coordinates = args


class Rectangle(Polygon):
    def __init__(self, x, y, width, height):
        super().__init__((x, y), (x + width, y + height))
        self.side_a = width
        self.side_b = height


class Square(Rectangle):
    def __init__(self, x, y, side_a):
        super().__init__(x, y, x + side_a, y + side_a)
