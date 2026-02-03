# Contributing to pfc-cli

First of all, thank you for taking the time to contribute!  
`pfc-cli` is a terminal-first data exploration and visualization tool for CSV files, and contributions of all kinds are welcome.

This document explains how to contribute effectively and responsibly.

---

## Ways to Contribute

You can contribute in several ways:

- 🐛 Reporting bugs
- ✨ Proposing or implementing new features
- 🧹 Improving code quality or performance
- 📚 Improving documentation or examples
- 🧪 Adding tests
- 🎨 Improving UI/UX of terminal output

---

## Getting Started (Development Setup)

### 1. Fork and clone the repository

```bash
git clone https://github.com/NNEngine/pfc-cli.git
cd pfc-cli
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install in editable mode

```bash
pip install -e .
```

This allows you to test changes instantly using:

```bash
pfc
```

---

## Project Structure Overview

```text
pfc/
├── commands/      # CLI commands (head, tail, groupby, plot, etc.)
├── core/          # Dataset abstraction and shared state
├── shell/         # REPL, command parser, dispatcher
├── ui/            # Rich-based rendering and styles
├── main.py        # Entry point
```

Please respect this separation of concerns when adding new features.

---

## Adding a New Command

1. Create a new file in `pfc/commands/`
2. Implement a `run(args)` function
3. Register the command in `shell/parser.py`
4. Add documentation to:

   * `help.py`
   * `README.md` (if user-facing)

Example command skeleton:

```python
def run(args):
    if session.df is None:
        console.print("[red]No dataset loaded[/red]")
        return
```

---

## Coding Guidelines

* Use **clear, readable Python**
* Avoid unnecessary abstractions
* Prefer explicit logic over clever tricks
* Handle errors gracefully (no uncaught tracebacks)
* Keep CLI output clean and consistent
* Use `rich` responsibly (no visual noise)

---

## Versioning Rules (Important)

* **Never modify an already released version**
* Always bump the version in `pyproject.toml`
* Follow semantic versioning loosely:

  * Patch: `0.1.x` → bug fixes
  * Minor: `0.x.0` → new features
  * Major: `1.0.0` → stable release

---

## Commit Message Style

Use clear, descriptive commit messages:

```text
fix: correct barplot rendering width
feat: add histogram command
docs: improve README examples
refactor: simplify dataset state handling
```

---

## Reporting Bugs

When reporting bugs, please include:

* OS and Python version
* `pfc-cli` version
* Command that caused the issue
* Full error message or screenshot (if applicable)
* Sample CSV (if possible)

---

## Feature Requests

Feature requests are welcome. Please describe:

* The problem you’re trying to solve
* Why it fits the philosophy of `pfc-cli`
* Example usage (CLI syntax preferred)

---

## Philosophy of the Project

`pfc-cli` aims to be:

* Terminal-first
* Lightweight
* Interactive
* Explicit over magical
* Useful for **exploration**, not heavy ETL

Please keep this philosophy in mind when proposing changes.

---

## Code of Conduct

Be respectful and constructive.
Harassment, discrimination, or toxic behavior will not be tolerated.

---

## Final Note

Even small contributions matter.
Documentation, feedback, and testing are just as valuable as code.

Thanks for helping make `pfc-cli` better 🚀
