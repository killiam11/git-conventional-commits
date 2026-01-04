# Open/Closed Principle (OCP)

## ❌ Problem

The `PaymentProcessor` class violates the Open/Closed Principle.

Every time a new payment method is required:
- The class must be modified
- Existing logic is at risk of breaking
- The system becomes harder to maintain

## ⚙️ Why this is bad

- High coupling
- Low extensibility
- Difficult to test and scale

The class is NOT closed for modification.
