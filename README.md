## walkertools
Python Utility and Style Functions 
## walkertools

A small, personal Python utility library.

This repository exists to hold **reusable helper code** that I write while learning Python, so I don’t copy-paste the same logic across projects. 
This is **not a framework** and **not a general-purpose library**. It is intentionally modest.

---

## Goals

- Keep code **DRY** across small scripts and projects
- Practice writing **clean, readable Python**
- Centralize simple helpers as they naturally emerge
- Improve over time as my understanding improves

Non-goals:

- Solving every problem with utilities
- Premature abstraction
- API stability
- Broad external usability

---

## What belongs here

Code that:
- Is small and self-contained
- Has been useful more than once
- Makes scripts easier to read
- Avoids hiding complexity

Examples:
- Simple CLI text formatting (banners, separators)
- Lightweight filesystem helpers
- Small string or data transformations
- Thin wrappers around standard-library behavior

---

## What does *not* belong here

- Business logic
- Project-specific code
- Large dependencies
- “Magic” helpers that obscure control flow
- Code I don’t yet understand

If a function feels confusing, it does not belong here yet.

---

## Installation
To install locally for development:
```bash
pip install -e .
