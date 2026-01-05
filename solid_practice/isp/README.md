# Interface Segregation Principle (ISP)

## Problem Description

The Worker interface defines multiple responsibilities:
working and eating.

Not all workers need all these behaviors.
For example, robots can work but do not eat.

## Why This Violates ISP

RobotWorker is forced to implement the eat method,
even though it does not need it.

This leads to:
- Unnecessary method implementations
- Runtime errors (NotImplementedError)
- Tight coupling between clients and unused methods

According to the Interface Segregation Principle,
clients should not be forced to depend on methods
they do not use.
