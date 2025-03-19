class Board:
    def __init__(self):
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.y = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
        self.x_size = 10
        self.y_size = 10
        self.size = f'{self.x_size} x {self.y_size}'
        self.color ='Grey'


class Ships(Board):
    def put(self,x, y):
        pass

class BLue_ships(Ships):
    def __init__(self):
        super().__init__()
        self.color = 'Blue'

class BLue_ships_5(BLue_ships):
    def __init__(self):
        super().__init__()
        self.size = 5
        self.quantity = 1

class BLue_ships_4(BLue_ships):
    def __init__(self):
        super().__init__()
        self.size = 4
        self.quantity = 1

class BLue_ships_3(BLue_ships):
    def __init__(self):
        super().__init__()
        self.size = 3
        self.quantity = 2

class BLue_ships_2(BLue_ships):
    def __init__(self):
        super().__init__()
        self.size = 2
        self.quantity = 2

class BLue_ships_1(BLue_ships):
    def __init__(self):
        super().__init__()
        self.size = 1
        self.quantity = 2

class Red_ships(Ships):
    def __init__(self):
        super().__init__()
        self.color = 'Red'

class Red_ships_5(Red_ships):
    def __init__(self):
        super().__init__()
        self.size = 5
        self.quantity = 1

class Red_ships_4(Red_ships):
    def __init__(self):
        super().__init__()
        self.size = 4
        self.quantity = 1

class Red_ships_3(Red_ships):
    def __init__(self):
        super().__init__()
        self.size = 3
        self.quantity = 2

class Red_ships_2(Red_ships):
    def __init__(self):
        super().__init__()
        self.size = 2
        self.quantity = 2

class Red_ships_1(Red_ships):
    def __init__(self):
        super().__init__()
        self.size = 1
        self.quantity = 2

