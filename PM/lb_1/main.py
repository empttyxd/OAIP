class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def start_engine(self):
        print('engine started')


class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count):
        super().__init__(max_speed, fuel_type)
        self.wheel_count = wheel_count

    def check_tires(self):
        print('wheels checked')


class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        super().__init__(max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0

    def load_cargo(self, weight):
            print('cargo loaded')


class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        super().__init__(max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity
        self.current_passengers = 0

    def board_passengers(self, count):
            print('passengers loaded')


class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight):
        WheeledVehicle.__init__(self, max_speed, fuel_type, wheel_count)
        CargoTransport.__init__(self, max_speed, fuel_type, cargo_capacity)
        self.max_weight = max_weight

    def reinforce_frame(self):
        print('frane reinfirced')


class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        super().__init__(max_speed, fuel_type)
        self.emission_level = emission_level

    def reduce_emission(self):
        print('emission reduced')


class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity,
                 max_weight, passenger_capacity, emission_level):
        HeavyDutyVehicle.__init__(self, max_speed, fuel_type, wheel_count,
                                  cargo_capacity, max_weight)
        PassengerTransport.__init__(self, max_speed, fuel_type, passenger_capacity)
        EcoFriendlyVehicle.__init__(self, max_speed, fuel_type, emission_level)








