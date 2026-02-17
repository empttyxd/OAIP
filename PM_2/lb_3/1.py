from abc import ABC, abstractmethod
from typing import Optional


class Transport(ABC):
    
    @abstractmethod
    def move(self) -> None:
        pass
    
    def start_journey(self) -> None:
        print(f"\n→ {self.__class__.__name__} начинает движение")
        self.prepare()
        self.move()
        self.finish()
    
    def prepare(self) -> None:
        print("Подготовка к поездке/полёту")
    
    def finish(self) -> None:
        print(" Поездка/полёт завершена.")

class Car(Transport):
    def move(self) -> None:
        print("Автомобиль едет по асфальту со скоростью 60–120 км/ч")


class Bicycle(Transport):
    def move(self) -> None:
        print("Велосипед движется за счёт педалей (макс. ~30–40 км/ч)")


class Plane(Transport):
    def prepare(self) -> None:
        print("Подготовка к полёту: проверка двигателей, взлётная полоса")
    
    def move(self) -> None:
        print(" Самолёт взлетает и летит на высоте 10 000 м со скоростью 850 км/ч")
    
    def finish(self) -> None:
        print("Посадка, заруливание на стоянку.")

class TransportFactory:
    
    @staticmethod
    def create(transport_type: str) -> Optional[Transport]:
        transport_type = transport_type.lower().strip()
        
        match transport_type:
            case "car" | "автомобиль" | "машина":
                return Car()
            case "bicycle" | "велосипед" | "bike":
                return Bicycle()
            case "plane" | "самолёт" | "airplane":
                return Plane()
            case _:
                print(f"Ошибка: неизвестный тип транспорта '{transport_type}'")
                return None

def demo():
    print("Демонстрация паттерна Factory Method (вариант 1)\n")
    
    requests = [
        "автомобиль",
        "велосипед",
        "самолёт",
        "поезд",        
        "plane",
        "BIKE",
    ]
    
    for req in requests:
        print(f"Запрос: {req}")
        transport = TransportFactory.create(req)
        
        if transport:
            transport.start_journey()
        print("-" * 65)


if __name__ == "__main__":
    demo()
