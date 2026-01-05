"""
Refactored SRP example.

Each class has a single responsibility.
"""

class UserRepository:
    def save(self, username: str, email: str) -> None:
        print(f"Saving {username} with {email} to database")


class EmailService:
    def send_welcome(self, email: str) -> None:
        print(f"Sending welcome email to {email}")


class UserService:
    def __init__(self, repository: UserRepository, email_service: EmailService):
        self.repository = repository
        self.email_service = email_service

    def create_user(self, username: str, email: str) -> None:
        print(f"Creating user {username}")
        self.repository.save(username, email)
        self.email_service.send_welcome(email)
