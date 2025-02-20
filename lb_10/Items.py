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

    def info(self):
        if self.status is True:
            print('Пассивная способность: Corruption\n'
                  'Атаки уменьшают броню цели на 6\n'
                  'Эффект длится 7 секунд')
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

    def info(self):
        if self.status is True:
            print('Пассивная способность: Bash\n'
                  'Каждая атака может оглушить цель на 1,2 сек. и нанести 100 физического урона. '
                  'Вероятность зависит от типа атаки владельца: 25% в ближнем бою, 10% — в дальнем.\n'
                  '+ 10 к силе\n'
                  '+ 30 к урону')
        else:
            print('У тебя нет предмета Skull Basher')

