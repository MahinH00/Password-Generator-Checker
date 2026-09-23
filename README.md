# Password-Generator-Checker
# Password Generator & Strength Checker

A lightweight, secure Python application designed to generate customizable, high-entropy passwords and evaluate the strength and complexity of existing credentials.

---

## Key Features

- **Configurable Password Generation**:
  - Custom length specification.
  - Granular character set toggles (uppercase letters, lowercase letters, numbers, and special symbols).
  - Cryptographically secure randomization to ensure unpredictability.

- **Password Strength Evaluation**:
  - Analyzes length, character diversity, and structure.
  - Flags weak patterns, sequential strings, and common dictionary vulnerabilities.
  - Provides real-time entropy calculation and complexity feedback (Weak, Moderate, Strong, Very Strong).

---

## Requirements

- Python 3.8+
- Standard library modules (no third-party dependencies required):
  - `secrets` / `random`
  - `string`
  - `re`

---

## How to Run

1. Clone or download the repository files.
2. Open a terminal or command prompt in this directory.
3. Run the script:
   ```bash
   python password_generator.py
