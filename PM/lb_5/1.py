from typing import Generic, TypeVar


T = TypeVar('T')


class Point(Generic[T]):
    def __init__(self, name: str, x: T, y: T, z: T):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'{self.name}({self.x}, {self.y}, {self.z})'


a1 = Point[int]('A', 1, 2, 3)
a2 = Point[float]('B', 1.1, 2.2, 3.3)
print(a1)
print(a2)
