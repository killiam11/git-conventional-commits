from abc import ABC, abstractmethod

"""
Good DIP example.

High-level and low-level modules
depend on an abstraction.
"""

class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailSender(MessageSender):
    def send(self, message: str) -> None:
        print(f"Sending email: {message}")


class NotificationService:
    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def notify(self, message: str) -> None:
        self.sender.send(message)


if __name__ == "__main__":
    sender = EmailSender()
    service = NotificationService(sender)
    service.notify("System alert")
