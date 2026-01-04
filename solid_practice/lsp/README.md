# Liskov Substitution Principle (LSP)

## Problem Description

The Square class inherits from Rectangle but breaks
the expected behavior of the base class.

A Rectangle allows width and height to change independently.
However, Square forces both values to remain equal.

This causes unexpected behavior when a Square instance
is used where a Rectangle is expected.

## Why This Violates LSP

Code that works correctly with Rectangle fails
when a Square is substituted.

This breaks the Liskov Substitution Principle, which states
that subclasses must be replaceable for their base classes
without altering the correctness of the program.
