class chest:
    def __init__(self):
        self.item = 'Sword'
        self.status = 'Locked'

    def open(self):
        if self.status == 'Locked':
            self.status = 'Unlocked'

    def take(self):
        if self.status == 'Locked':
            print('You cant take anything')
        else:
            print('Now you have a good sword!')
            self.item = 'Empty'
