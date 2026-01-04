class UserManager:
    def __init__(self):
        self.users = []
        
    def add_user(self, name, email):
        self.users.append({"name": name, "email": email})
        print(f"User {name} added")
    
    def save_users_to_file(self):
        with open("users.txt", "w") as file:
            for user in self.users:
                file.write(f"{user['name']} - {user['email']}\n")
    
    def send_welcome_email(self, email):
        print(f"Sending welcome email to {email}")
        