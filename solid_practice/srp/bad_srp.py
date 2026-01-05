"""
Bad SRP example.

This class handles:
- user data
- saving to database
- sending email notifications
"""

class UserManager:
    def create_user(self, username: str, email: str) -> None:
        print(f"Creating user {username}")
        self._save_to_database(username, email)
        self._send_welcome_email(email)

    def _save_to_database(self, username: str, email: str) -> None:
        print(f"Saving {username} with {email} to database")

    def _send_welcome_email(self, email: str) -> None:
        print(f"Sending welcome email to {email}")
