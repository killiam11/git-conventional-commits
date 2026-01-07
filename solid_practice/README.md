# SOLID Practice

This folder contains **practical examples of the SOLID principles**, focused on
learning through contrast: *what not to do* vs *how to do it correctly*.

Each principle is explored with **intentionally bad designs** and their
**refactored counterparts**, making the reasoning behind each rule explicit.

---

## 📄 What Is SOLID?

SOLID is a set of five object-oriented design principles that help create
software that is:

- Easier to understand
- Easier to maintain
- Easier to extend
- Less fragile to change

A general conceptual introduction to SOLID lives in the `intro/` folder.

---

## 📁 Folder Structure

```text
solid_practice/
├── README.md        # This file (overview and navigation)
├── intro/           # Conceptual introduction to SOLID
│   ├── README.md
│   ├── bad_design.py
│   └── refactored_design.py
├── srp/             # Single Responsibility Principle
│   ├── README.md
│   ├── bad_srp.py
│   └── refactored_srp.py
├── ocp/             # Open/Closed Principle
│   ├── README.md
│   ├── bad_ocp.py
│   └── refactored_ocp.py
├── lsp/             # Liskov Substitution Principle
│   ├── README.md
│   ├── bad_lsp.py
│   └── refactored_lsp.py
├── isp/             # Interface Segregation Principle
│   ├── README.md
│   ├── bad_isp.py
│   └── refactored_isp.py
└── dip/             # Dependency Inversion Principle
    ├── README.md
    ├── bad_dip.py
    └── refactored_dip.py
