"""
Bad OCP example.
This payment processor must be modified
every time a new payment method is added.
"""

class PaymentProcessor:
    def process(self, payment_type: str, amount: float) -> None:
        if payment_type == "credit_card":
            print(f"Procesing credit card payment of ${amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of ${amount}")
        else:
            raise ValueError("Unsupported payment method")
    