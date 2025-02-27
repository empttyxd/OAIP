class Desolator():
    def __init__(self):
        self.status = False
        self.Mithril_Hammer = 0
        self.Bright_stone = 0

    def buy(self,name, a):
        self.name = name
        if name == 'Mithril hammer':
            self.Mithril_Hammer += a
        elif name == 'Bright stone':
            self.Bright_stone += a
        else:
            print('Ошибка')

    def craft(self):
        if self.Mithril_Hammer >= 2 and self.Bright_stone >= 1:
            self.status = True
            self.Mithril_Hammer -= 2
            self.Bright_stone -= 1
        else:
            print('Ошибка.Не достаточно предметов для крафта')

    def info(self):
        if self.status is True:
            print('Пассивная способность: Corruption\n'
                  'Атаки уменьшают броню цели на 6\n'
                  'Эффект длится 7 секунд\n\n'
                  'Пассивная способность: Soul stealer\n'
                  'Когда умирает герой, броня которого была уменьшена этим предметом, бонус к урону увеличивается на 2.\n'
                  'Максимум: 30 урона.\n\n'
                  'Бонусы:\n'
                  '+50 к урону')
        else:
            print('У тебя нет предмета Desolator')

class Skull_basher():
    def __init__(self):
        self.status = False
        self.Mithril_Hammer = 0
        self.Belt_of_strength = 0
        self.recept = 0

    def buy(self,name, a):
        self.name = name
        if name == 'Mithril hammer':
            self.Mithril_Hammer += a
        elif name == 'Belt of strength':
            self.Belt_of_strength += a
        elif name == 'Recept':
            self.recept += a
        else:
            print('Ошибка')

    def craft(self):
        if self.Mithril_Hammer >= 1 and self.Belt_of_strength >= 1 and self.recept >= 1:
            self.status = True
            self.Mithril_Hammer -= 1
            self.Belt_of_strength -= 1
            self.recept -= 1
        else:
            print('Ошибка.Не достаточно предметов для крафта')


    def info(self):
        if self.status is True:
            print('Пассивная способность: Bash\n'
                  'Каждая атака может оглушить цель на 1,2 сек. и нанести 100 физического урона. '
                  'Вероятность зависит от типа атаки владельца: 25% в ближнем бою, 10% — в дальнем.\n\n'
                  'Бонусы:\n'
                  '+ 10 к силе\n'
                  '+ 30 к урону')
        else:
            print('У тебя нет предмета Skull Basher')

class Butterfly():
    def __init__(self):
        self.status = False
        self.Eaglesong = 0
        self.Talisman_of_evasion = 0
        self.Claymore = 0

    def buy(self,name, a):
        self.name = name
        if name == 'Eaglesong':
            self.Eaglesong += a
        elif name == 'Talisman of evasion':
            self.Talisman_of_evasion += a
        elif name == 'Claymore':
            self.Claymore += a
        else:
            print('Ошибка')

    def craft(self):
        if self.Eaglesong >= 1 and self.Talisman_of_evasion>= 1 and self.Claymore >= 1:
            self.status = True
            self.Eaglesong -= 1
            self.Talisman_of_evasion -= 1
            self.Claymore -= 1
        else:
            print('Ошибка.Не достаточно предметов для крафта')

    def info(self):
        if self.status is True:
            print('Бонусы:\n'
                  '+25 к урону\n'
                  '+35% к уклонению\n'
                  '+20% базовой скорости атаки\n'
                  '+35 к ловковсти')
        else:
            print('У тебя нет предмета Butterfly')

