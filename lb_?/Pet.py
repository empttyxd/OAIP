class pet:
    def __init__(self):
        self.born_status = False
        self.age_status = 'None'
        self.name = 'None'
        self.hungry_status = 'None'
        self.thirsty_status = 'None'
        self.sleep_status = 'None'
        self.health_status = 'None'

    def born(self):
        if self.born_status is False:
            self.born_status = True
            self.age_status = 'Kid'
            self.hungry_status = 'Hungry'
            self.thirsty_status = 'Thirsty'
            self.sleep_status = 'Tired'
            self.health_status = 'Health'

    def name(self, pet_name):
        if self.born_status != 'Dead xd':
            if self.born_status is True:
                self.name = pet_name
            else:
                print('Your pet has not yet been born')
        else:
            print('Your pet is gone')

    def eat(self):
        if self.born_status != 'Dead xd':
            if self.born_status is True:
                if self.hungry_status == 'Hungry':
                    self.hungry_status = 'Well fed'
                else:
                    print('Your pet is not hungry')
            else:
                print('Your pet has not yet been born')
        else:
            print('Your pet is gone')



    def drink(self):
        if self.born_status != 'Dead xd':
            if self.born_status is True:
                if self.thirsty_status == 'Thirsty':
                    self.thirsty_status = 'Not thirsty'
                else:
                    print('Your pet is not thirsty')
            else:
                print('Your pet has not yet been born')
        else:
            print('Your pet is gone')

    def sleep(self):
        if self.born_status != 'Dead xd':
            if self.born_status is True:
                if self.sleep_status == 'Tired':
                    self.sleep_status = 'Pepful'
                else:
                    print('Your pet doesnt want to sleep')
            else:
                print('Your pet has not yet been born')
        else:
            print('Your pet is gone')

    def grow_up(self):
        if self.born_status != 'Dead xd':
            if self.born_status is True:
                if self.age_status == 'Kid':
                    self.age_status = 'Teen'
                elif self.age_status == 'Teen':
                    self.age_status = 'Adult'
                elif self.age_status == 'Adult':
                    self.age_status = 'Old'
                elif self.age_status == 'Old':
                    self.age_status = 'Dead'
                    self.health_status = 'Death'
                    self.name = 'Your pet is gone'
                    self.hungry_status = 'Your pet is gone'
                    self.thirsty_status = 'Your pet is gone'
                    self.sleep_status = 'Your pet is gone'
                    self.born_status = 'Dead xd'
            else:
                print('Your pet has not yet been born')
        else:
            print('Your pet is gone')
