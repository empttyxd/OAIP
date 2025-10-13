class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.engine = False
        self.max_speed = max_speed
        self.fuel_type = fuel_type
    def start_engine(self):
        self.engine = True
        print('engine is running')


class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.wheel_count = wheel_count

    def check_tires(self):
        print('tires checked')


class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity
        self.cargo = 0

    def load_cargo(self, num):
        if self.cargo + num > self.cargo_capacity:
            print('not enough space for cargo')
        else:
            self.cargo += num
            print('сargo loaded:', self.cargo)


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity
        self.passenger = 0

    def board_passengers(self, people):
        if self.passenger + people > self.passenger_capacity:
            print('Not enough seats for passengers')
        else:
            self.passenger += people
            print('Passengers in transport:', self.passenger)


class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight):
        WheeledVehicle.__init__(self, max_speed, fuel_type, wheel_count)
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)
        self.max_weight = max_weight

    def reinforce_frame(self):
        print('The transport frame is reinforced')


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        Vehicle.__init__(self, max_speed, fuel_type)
        self.emission_level = emission_level

    def reduce_emission(self):
        self.emission_level -= 1
        print('Current level:', self.emission_level)


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity,
                 max_weight, passenger_capacity, emission_level):
        HeavyDutyVehicle.__init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight)
        PassengerTransport.__init__(self, max_speed, fuel_type, passenger_capacity)
        EcoFriendlyVehicle.__init__(self, max_speed, fuel_type, emission_level)

    def status(self):
        print(f'''Скорость: {self.max_speed}
        Тип топлива: {self.fuel_type}
        Груз: {self.cargo}
        Пассажиры: {self.passenger}
        Уровень выбросов: {self.emission_level}''')









