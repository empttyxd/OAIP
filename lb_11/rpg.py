class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = 10
        self.stamina = 100

    def attack(self):
        print(f'Вы нанесли {self.attack_power} урона')
        
    def info(self):
        print(f'Имя: {self.name}\n'
              f'Здоровье: {self.hp}\n'
              f'Сила атака: {self.attack_power}\n'
              f'Выносливость: {self.stamina}')

class Warrior(Character):
    def __init__(self):
        self.rage_ = 0
        self.rage_flag = False

    def attack(self):
        if self.rage_flag == False:
            print(f'Вы ударили мечом, нанеся {super().attack_power}')
            if self.rage_ < 100:
                self.rage_ += 10
            else:
                self.rage_ += 0
        else:
            print(f'Вы ударили мечом, нанеся {super().attack_power}')
            self.rage_ -= 10
            if self.rage_ == 0:
                super().attack_power == 10
            

    def rage(self):
        if self.rage_ == 100:
            self.rage_flag = True
            print("Вы активировали ярость, сила атаки увеличина")
            # super().attack_power == 50
        else:
            print('Не хватает очков ярости')
        



