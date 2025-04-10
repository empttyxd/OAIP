class Inventory:
    def __init__(self):
        self.__items = {'Sword': 1, 'Gold': 100, 'asd': 3}
        self.__weight_limit = 100
        self.__slots = 10
        self.__current_weight = 50

    def __str__(self):
        return f'inventory\nslots: {self.__slots}\n' \
               f'items: {self.__items}\n' \
               f'weight: {self.__current_weight}\n' \
               f'weight limit: {self.__weight_limit}'


    def __iter__(self):
        return self.__items.__iter__()

    def __len__(self):
        return self.__items.__len__()

    def __getitem__(self, item):
        return self.__items[item]

    def __setitem__(self, key, value):
        if len(self.__items) < self.__slots:
            self.__items.__setitem__(key, value)
        else:
            print('Инвентарь переполнен')

    def __delitem__(self, key):
        self.__items.__delitem__(key)

    def __contains__(self, item):
        self.__items.__contains__(self.__items[item])
        if item in self.__items:
            print(f'{item} в инвентаре')
        else:
            print(f'{item} не в инвентаре')













a = Inventory()
a.__contains__('asd')
