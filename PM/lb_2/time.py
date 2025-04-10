class Seconds:
    def __init__(self):
        self.__seconds = 15

    def __str__(self):
        print(self.__seconds.__str__() + 's')

    def __int__(self):
        print(self.__seconds.__int__())

class Minutes:
    def __init__(self):
        self.__minutes = 30

    def __str__(self):
        print(self.__minutes.__str__() + 'm')

    def __int__(self):
        print(self.__minutes.__int__())

class Hours:
    def __init__(self, h):
        self.__hours = h

    def __str__(self):
        return str(self.__hours)

    def __int__(self):
        return self.__hours


class Times(Seconds, Minutes, Hours):
    def __init__(self, seconds = 0):
        super().__init__()
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def __str__(self):
        print(Hours.__str__(), Minutes.__str__(), Seconds.__str__())


