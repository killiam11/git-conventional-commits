# Single Responsibility Principle (SRP)

## ❌ Problem

The `UserManager` class has multiple responsibilities:

- Creating users
- Persisting data
- Sending emails

This violates the Single Responsibility Principle because the class has
more than one reason to change.
