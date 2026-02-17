from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата {amount:.2f} ₽ картой — успешно"


class EWalletPayment(PaymentMethod):
    def pay(self, amount: float) -> str:
        return f"Оплата {amount:.2f} ₽ через кошелёк — успешно"


class PaymentPlatform(ABC):
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    @abstractmethod
    def process_payment(self, amount: float, order_id: str) -> str:
        pass


class MobileAppPlatform(PaymentPlatform):
    def process_payment(self, amount: float, order_id: str) -> str:
        result = self.payment_method.pay(amount)
        return f"[Мобильное приложение] Заказ #{order_id}\n→ {result}"


class WebPlatform(PaymentPlatform):
    def process_payment(self, amount: float, order_id: str) -> str:
        result = self.payment_method.pay(amount)
        return f"[Веб-сайт] Заказ #{order_id}\n→ {result}"


if __name__ == "__main__":
    card = CreditCardPayment()
    wallet = EWalletPayment()

    mobile = MobileAppPlatform(card)
    web = WebPlatform(wallet)

    print(mobile.process_payment(2490.00, "ORD-12345"))
    print("-" * 50)
    print(web.process_payment(1350.50, "ORD-67890"))
    print("-" * 50)

    web.payment_method = card
    print(web.process_payment(4780.00, "ORD-99999"))
    print("-" * 50)

    mobile.payment_method = wallet
    print(mobile.process_payment(890.00, "ORD-11111"))
