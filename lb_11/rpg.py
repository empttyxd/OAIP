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
        super().__init__(self)
        self.rage_ = 0
        self.rage_flag = False

    def attack(self):
        if self.rage_flag is False:
            print(f'Вы ударили мечом, нанеся {self.attack_power} урона')
            if self.rage_ < 100:
                self.rage_ += 10
            else:
                self.rage_ += 0
        else:
            print(f'Вы ударили мечом, нанеся {self.attack_power} урона')
            self.rage_ -= 10
            if self.rage_ == 0:
                self.attack_power = 10
                self.rage_flag = False
            

    def rage(self):
        if self.rage_ == 100:
            self.rage_flag = True
            print("Вы активировали ярость, сила атаки увеличина")
            self.attack_power = 50
        else:
            print('Не хватает очков ярости')

    def heal(self):
        if self.rage_ >= 10:
            if self.hp < 100:
                self.hp += 10
                self.rage_ -= 10
            else:
                self.hp += 0
                self.rage_ -= 10
        else:
            print("Не достаточно очков ярости")

class Mage(Character):
    def __init__(self):
        super().__init__(self)
        self.mana = 100

    def attack(self):
        if self.mana > 0:
            print(f'Вы атаковали магией, нанеся {self.attack_power * 2} урона')
            self.mana -= 10
        else:
            print(f'Не хватает очков маны')

    def fireball(self):
        if self.mana >= 50:
            print(f'Использована способность fireball, вы нанесли 100 урона')
            self.mana -= 50
        else:
            print("Не хватает очков маны")

    def mana_regen(self):
        while self.mana < 100:
            self.mana += 10

class Archer(Character):
    def __init__(self):
        super().__init__(self)
        self.arrows = 100

    def attack(self):
        if self.arrows > 0:
            print(f'Вы выстрелили из лука, нанеся {self.attack_power} урона')
            self.arrows -= 1
        else:
            print("У вас нет стрел")

    def volley(self):
        if self.arrows > 0:
            print(f'Залп! Вы нанесли {self.attack_power * 5}')
            self.arrows -= 10
        else:
            print("У вас нет стрел")
            
    def create(self):
        while self.arrows < 100:
            self.arrows += 10
        



