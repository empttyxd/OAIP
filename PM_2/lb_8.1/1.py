from abc import ABC, abstractmethod
from typing import List


class Customer(ABC):
    @abstractmethod
    def update(self, product_name: str, price: float) -> None:
        pass


class RegularCustomer(Customer):
    def __init__(self, name: str):
        self.name = name

    def update(self, product_name: str, price: float) -> None:
        print(f"  [{self.name}] Новый товар в магазине: {product_name} — {price} ₽")


class VipCustomer(Customer):
    def __init__(self, name: str):
        self.name = name

    def update(self, product_name: str, price: float) -> None:
        print(f"  [{self.name} VIP] Новинка: {product_name} всего за {price} ₽ — уже в пути? 😏")


class WishlistCustomer(Customer):
    def __init__(self, name: str, interested_in: str):
        self.name = name
        self.interested_in = interested_in.lower()

    def update(self, product_name: str, price: float) -> None:
        if self.interested_in in product_name.lower():
            print(f"  [{self.name}] Внимание! Появился {product_name} ({price} ₽) — именно то, что вы ждали!")


class Store:
    def __init__(self, name: str):
        self.name = name
        self._customers: List[Customer] = []
        self._products: List[tuple[str, float]] = []

    def attach(self, customer: Customer) -> None:
        if customer not in self._customers:
            self._customers.append(customer)
            print(f"→ {getattr(customer, 'name', 'Клиент')} подписался на уведомления магазина {self.name}")

    def detach(self, customer: Customer) -> None:
        if customer in self._customers:
            self._customers.remove(customer)
            print(f"→ {getattr(customer, 'name', 'Клиент')} отписался от уведомлений")

    def add_product(self, name: str, price: float) -> None:
        self._products.append((name, price))
        print(f"\nМагазин '{self.name}' добавил товар: {name} — {price} ₽")
        self._notify(name, price)

    def _notify(self, product_name: str, price: float) -> None:
        for customer in self._customers:
            customer.update(product_name, price)


if __name__ == "__main__":
    store = Store("TechNova")

    anna = RegularCustomer("Анна")
    maxim = VipCustomer("Максим")
    dmitry = WishlistCustomer("Дмитрий", "наушники")
    elena = WishlistCustomer("Елена", "смартфон")

    store.attach(anna)
    store.attach(maxim)
    store.attach(dmitry)
    store.attach(elena)

    print("\n" + "="*60)

    store.add_product("Беспроводные наушники Sony WH-1000XM5", 32990)
    print("-"*60)

    store.add_product("Смартфон iPhone 16 Pro 256GB", 129990)
    print("-"*60)

    store.add_product("Ноутбук MacBook Air M3", 98900)
    print("-"*60)

    store.add_product("Игровые наушники HyperX Cloud Alpha", 8990)
    print("-"*60)

    store.detach(maxim)
    print("\nМаксим отписался от рассылки\n")

    store.add_product("Планшет Samsung Galaxy Tab S10", 74990)
