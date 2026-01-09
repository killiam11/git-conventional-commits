# Dependency Inversion Principle (DIP)

This example demonstrates a violation of the Dependency Inversion Principle
and how it can be resolved through proper abstractions.

## Problem Description

The high-level `NotificationService` depends directly on a concrete
implementation such as `EmailService`.

This creates a rigid design where changing the notification channel
requires modifying the high-level logic.

## Why This Violates DIP

- High-level modules depend on low-level modules
- There is no abstraction separating policy from implementation
- The system becomes hard to test and extend

According to the Dependency Inversion Principle:

- High-level modules should not depend on low-level modules
- Both should depend on abstractions
