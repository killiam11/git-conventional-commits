# SOLID Practice

This module demonstrates how poor object-oriented design can be improved
by applying the SOLID principles.

## Initial Design Problems

The initial `UserManager` implementation violates several SOLID principles:

### Single Responsibility Principle (SRP)
- The class is responsible for:
  - Managing user data
  - Persisting users to a file
  - Sending emails

### Open/Closed Principle (OCP)
- Changing the persistence mechanism or email logic
  requires modifying the `UserManager` class.

### Dependency Inversion Principle (DIP)
- The class depends directly on low-level details
  such as file handling and email delivery.
