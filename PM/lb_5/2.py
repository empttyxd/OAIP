from typing import Generic, TypeVar


A = TypeVar('T')


class TypedArray(Generic[A]):
    def __init__(self):
        self.array = []

    def add(self, item: A):
        self.array.append(item)

    def get(self, index):
        if -len(self.array) <= index < len(self.array):
            return self.array[index]
        else:
            return 'Выход за пределы'

    def __str__(self):
        return str(self.array)


a = TypedArray[int]()
a.add(1)
a.add(2)
a.add(3)
print(a)
a.add(4)
print(a.get(-3))
print(a.get(3))
