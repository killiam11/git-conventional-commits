"""
Bad DIP example.

The high-level NotificationService
depends directly on a concrete EmailService.
"""

class EmailService:
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")


class NotificationService:
    def __init__(self) -> None:
        self.email_service = EmailService()

    def notify(self, message: str) -> None:
        self.email_service.send(message)


if __name__ == "__main__":
    service = NotificationService()
    service.notify("System alert")
