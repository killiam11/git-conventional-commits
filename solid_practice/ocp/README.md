# Open/Closed Principle (OCP)

This example shows how modifying existing code to add new behavior
leads to fragile and unscalable designs.

## Problem Description

The `PaymentProcessor` class requires modification
every time a new payment method is introduced.

## Why This Violates OCP

- Existing code must be changed to extend functionality
- The risk of introducing regressions increases
- The system becomes harder to test and maintain

> The Open/Closed Principle states that:
software entities should be open for extension
but closed for modification.
