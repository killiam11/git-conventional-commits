# SOLID — Introduction

This folder serves as an entry point to the SOLID principles.

It demonstrates how a naive object-oriented design can evolve into a cleaner,
more maintainable architecture by applying SOLID concepts incrementally.

## What This Folder Contains

This module includes:

- A **bad design example** that intentionally violates multiple SOLID principles
- A **refactored version** showing how those issues can be addressed
- A conceptual bridge between theory and the principle-specific examples
  found in the other folders

## Common Design Issues Shown

The initial design highlights several typical problems found in early OOP code:

### Single Responsibility Principle (SRP)
- One class handling multiple responsibilities:
  - Domain logic
  - Persistence
  - External services (e.g. notifications)

### Open/Closed Principle (OCP)
- Core logic must be modified when adding new behavior
- No clear extension points

### Dependency Inversion Principle (DIP)
- High-level logic depends directly on low-level implementations
- No abstractions separating policies from details

## Why This Matters

Before studying each SOLID principle in isolation, it is important to see
how they interact in a real piece of code.

This folder provides that initial context.

## Next Steps

- See `srp/` for a focused exploration of Single Responsibility
- See `ocp/`, `lsp/`, `isp/`, and `dip/` for deeper, isolated examples
