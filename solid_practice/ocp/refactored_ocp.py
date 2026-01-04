"""
Refactored OCP example.

New payment methods can be added
without modifying existing code.
"""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")


class PaymentProcessor:
    def process(self, payment_method: PaymentMethod, amount: float) -> None:
        payment_method.pay(amount)
