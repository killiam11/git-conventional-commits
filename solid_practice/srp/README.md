# Single Responsibility Principle (SRP)

This example highlights how combining multiple responsibilities
into a single class leads to tightly coupled and fragile code.

## Problem Description

The `UserManager` class is responsible for:

- Creating users
- Persisting user data
- Sending notifications

## Why This Violates SRP

- The class has multiple reasons to change
- Changes in one concern affect unrelated behavior
- The code becomes harder to maintain and test

> The Single Responsibility Principle states that:
a class should have one, and only one, reason to change.
