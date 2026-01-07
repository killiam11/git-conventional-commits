from abc import ABC, abstractmethod

# SRP: User entity only holds data
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

# OCP + DIP: abstraction for persistence
class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass
    
class FileUserRepository(UserRepository):
    def save(self, user: User):
        with open("users.txt", "a") as file:
            file.write(f"{user.name} - {user.email}\n")

# SRP: email responsibility only
class EmailService:
    def send_welcome_email(self, email: str):
        print(f"Sending welcome email to {email}")

# SRP: orchestrates use cases
class UserService:
    def __init__(self, repository: UserRepository, email_service: EmailService):
        self.repository = repository
        self.email_service = email_service
    
    def register_user(self, user: User):
        self.repository.save(user)
        self.email_service.send_welcome_email(user.email)
        
        
