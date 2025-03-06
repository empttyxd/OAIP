class chest:
    def __init__(self):
        self.items = ['Gold 500', 'Sword', 'Armor', 'Rotten apple']
        self.status = 'Locked'
        self.capacity = 10

    def info(self):
        if len(self.items) > 0:
            for i in range(len(self.items)):
                print(f'{i + 1}) {self.items[i]}')
        else:
            print('Chest is empty')

    def open(self):
        if self.status == 'Locked':
            self.status = 'Unlocked'

    def lock(self):
        if self.status == 'Unlocked':
            self.status = 'Locked'


    def take(self, *args):
        if self.status == 'Locked':
            print('You cant take anything')

        else:
            for i in range(len(args) - 1, -1, -1):
                print(f'You take:{self.items[args[i] - 1]}')
                self.items.pop(args[i] - 1)

    def take_all(self):
        print('You take everything')
        self.items.clear()

    def put(self, *args):
        for i in range(len(args)):
            self.items.append(args[i])
            if len(self.items) > self.capacity:
                print('Chest if full')
                break
