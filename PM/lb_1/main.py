class Vehicle:
    def __init__(self, max_speed, fuel_type):
        self.max_speed = max_speed
        self.fuel_type = fuel_type
        print(f"🚗 Создан транспорт: {max_speed} км/ч, {fuel_type}")

class WheeledVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, wheel_count):
        super().__init__(max_speed, fuel_type)
        self.wheel_count = wheel_count
        print(f"   👉 {wheel_count} колёс")

class CargoTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, cargo_capacity):
        super().__init__(max_speed, fuel_type)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0
        print(f"   📦 {cargo_capacity} кг")

class HeavyDutyVehicle(WheeledVehicle, CargoTransport):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, max_weight):
        super().__init__(max_speed, fuel_type, wheel_count, cargo_capacity)
        self.max_weight = max_weight
        print(f"   💪 {max_weight} тонн")

class PassengerTransport(Vehicle):
    def __init__(self, max_speed, fuel_type, passenger_capacity):
        super().__init__(max_speed, fuel_type)
        self.passenger_capacity = passenger_capacity
        self.current_passengers = 0
        print(f"   👥 {passenger_capacity} мест")

class EcoFriendlyVehicle(Vehicle):
    def __init__(self, max_speed, fuel_type, emission_level):
        super().__init__(max_speed, fuel_type)
        self.emission_level = emission_level
        print(f"   🌿 {emission_level} г/км")

class HybridDeliveryVan(HeavyDutyVehicle, PassengerTransport, EcoFriendlyVehicle):
    def __init__(self, max_speed, fuel_type, wheel_count, cargo_capacity, 
                 max_weight, passenger_capacity, emission_level):
        super().__init__(max_speed, fuel_type, wheel_count, cargo_capacity, 
                        max_weight, passenger_capacity, emission_level)
        print("🎉 ГИБРИДНЫЙ ФУРГОН СОЗДАН!")







