from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        pass
    
    @abstractmethod
    def get_name(self) -> str:
        pass


class CourierDelivery(DeliveryStrategy):
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        base_price = 300
        per_km = 25
        per_kg = 40
        weight_fee = max(0, weight_kg - 2) * per_kg
        return round(base_price + distance_km * per_km + weight_fee, 2)
    
    def get_name(self) -> str:
        return "Курьерская доставка"


class PostalDelivery(DeliveryStrategy):
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        base = 180
        per_kg = 65
        distance_factor = 1 + (distance_km / 1000) * 0.4
        return round(base + weight_kg * per_kg * distance_factor, 2)
    
    def get_name(self) -> str:
        return "Почтовая доставка"


class DroneDelivery(DeliveryStrategy):
    def calculate_cost(self, weight_kg: float, distance_km: float) -> float:
        if weight_kg > 5:
            raise ValueError("Дрон не может нести посылку тяжелее 5 кг")
        if distance_km > 30:
            raise ValueError("Дрон не доставляет дальше 30 км")
        
        base = 450
        per_km = 35
        weight_bonus = 80 if weight_kg > 2 else 0
        return round(base + distance_km * per_km + weight_bonus, 2)
    
    def get_name(self) -> str:
        return "Доставка дроном"


@dataclass
class Order:
    weight_kg: float
    distance_km: float
    description: str = "Посылка"


class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        self._strategy: Optional[DeliveryStrategy] = None
        self.set_strategy(strategy)
    
    def set_strategy(self, strategy: DeliveryStrategy) -> None:
        self._strategy = strategy
    
    def calculate_delivery_cost(self, order: Order) -> float:
        try:
            return self._strategy.calculate_cost(order.weight_kg, order.distance_km)
        except ValueError:
            return float('inf')


if __name__ == "__main__":
    order = Order(weight_kg=3.5, distance_km=45)
    
    context = DeliveryContext(CourierDelivery())
    
    for strategy in [CourierDelivery(), PostalDelivery(), DroneDelivery()]:
        context.set_strategy(strategy)
        cost = context.calculate_delivery_cost(order)
        print(f"{strategy.get_name():<22} → {cost:>7.2f} ₽")
