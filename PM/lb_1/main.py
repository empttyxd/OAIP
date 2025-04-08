class Vehicle:
    def __init__(self):
        self.max_speed = 150
        self.fuel_type = 'asd'
        self.engine = False


    def start_engine(self):
        if self.engine == False:
            self.engine = True

class WheeledVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        self.wheel_count = 4
        self.tires_status = 100

    def check_tires(self):
        print(self.tires_status, end='%')

class CargoTransport(Vehicle):
    def __init__(self):
        super().__init__()
        self.cargo_capacity = 200
        self.cargo_weight = 1

    def load_cargo(self, a):
        if self.cargo_weight < self.cargo_capacity:
            self.cargo_weight += a
        else:
            print('Перегрузка')

class PassengerTransport(Vehicle):
    def __init__(self):
        super().__init__()
        self.passengers_capacity = 100
        self.passengers = 1

    def board_passangers(self, a):
        if self.passengers < self.passengers_capacity:
            self.passengers += a
        else:
            print('Нет места')

class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self):
        super().__init__()
        self.max_weight = 400
        self.frame = 'standart frame'

    def reinforce_frame(self):
        self.frame = 'reinforce frame'

class EcoFriendlyVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        self.emission_level = 100

    def reduce_emission(self, a):
        self.emission_level -= a

class HybridDeliveryVan(HeavyDutyVehicle, EcoFriendlyVehicle, PassengerTransport):
    pass

    def status(self):
        print(f'Скорость: {self.max_speed}\n'
              f'Топливо: {self.fuel_type}\n'
              f'Пассажиры: {self.passengers}\n'
              f'Выбросы: {self.emission_level}')










