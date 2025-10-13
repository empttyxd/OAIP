from abc import ABC, abstractmethod


class GameItem(ABC):
    def __init__(self, item_name, weight, rarity):
        self.item_name = item_name
        self.weight = weight
        self.rarity = rarity

    @abstractmethod
    def use(self):
        pass

    def get_description(self):
        return f'"{self.item_name}" (Rarity: {self.rarity}, Weight: {self.weight})'


class HealthPotion(GameItem):
    def __init__(self, item_name, weight, rarity):
        super().__init__(item_name, weight, rarity)

    def use(self):
        return f'Health potion used: +50 HP'

    def get_description(self):
        return f'healt potion {super().get_description()} - restores 50 HP'


class ManaCrystal(GameItem):
    def __init__(self, item_name, weight, rarity):
        super().__init__(item_name, weight, rarity)

    def use(self):
        print(f'Mana Crystal used: +30 MP')

    def get_description(self):
        return f'mana crystal {super().get_description()} - restores 30 MP'

