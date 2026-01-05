# Dependency Inversion Principle (DIP)

## Problem

The `NotificationService` depends directly on `EmailService`.

This creates tight coupling and makes the system hard to extend
or test with different notification channels.

## Violation

- High-level modules depend on low-level modules
- No abstraction between services
