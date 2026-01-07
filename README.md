# Git Conventional Commits

This repository documents my learning process around **Git best practices**,
**Conventional Commits**, and **software design principles**.

The focus is not only on code, but on how changes are introduced and explained
through commits.

## What Is Practiced Here

### Conventional Commits
- feat / fix / refactor / chore / docs
- scopes and intent-based commit messages
- readable and meaningful history

### Commit Validation
- Commit messages are validated using **commitlint**
- Git hooks are enforced with **Husky**
- Invalid commits are blocked automatically

> Tooling configuration lives at the repository root, while Git hooks are
> isolated inside the `.husky/` directory.


### Semantic Versioning
- Versions are generated from commits
- CHANGELOG.md is built automatically
- Git tags follow SemVer (vX.Y.Z)

### SOLID Principles
Inside the `solid_practice/` folder, each principle is explored with:

- Bad design examples (intentionally incorrect)
- Refactored versions applying the principle

Covered principles:
- SRP – Single Responsibility
- OCP – Open/Closed
- LSP – Liskov Substitution
- ISP – Interface Segregation
- DIP – Dependency Inversion

### Experiments
The `experiments/` folder contains small scripts and tests used to validate
concepts or workflows.

## Structure Overview



```text
.
├── .husky/
│   └── commit-msg          # Git hook enforcing commit message rules
│
├── experiments/
│   ├── README.md           # Explanation of experiments purpose
│   └── test_1.py           # Isolated tests and learning scripts
│
├── solid_practice/
│   ├── intro/              # Basic design vs refactored examples
│   ├── srp/                # Single Responsibility Principle
│   ├── ocp/                # Open/Closed Principle
│   ├── lsp/                # Liskov Substitution Principle
│   ├── isp/                # Interface Segregation Principle
│   └── dip/                # Dependency Inversion Principle
│
├── .gitignore
├── CHANGELOG.md            # Generated from conventional commits
├── commitlint.config.js    # Commit message validation rules
├── package.json            # Tooling dependencies and scripts
├── package-lock.json
└── README.md               # Project documentation
`````
## Purpose

This repository exists to learn by doing and to maintain a clear learning history
through meaningful commits.

### Philosophy

- Code changes are temporary.  
- Commit history is permanent.
- Treats commits as first-class documentation.