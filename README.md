# 🤖 Robotic Sorting System

This project simulates a robotic arm in a factory that classifies packages based on their volume and mass. It includes two versions of the solution: a simple function and an object-oriented implementation using a `Package` class.

---

## 📂 Project Structure

### Basic Version

The `main.py` file contains the basic solution to the challenge:

- Implements the `sort(width, height, length, mass)` function.
- Includes simple `assert` tests to verify behavior.

#### 📌 Usage

1. Open `main.py`.
2. Run the file with:

   ```bash
   python main.py
   ```

3. Modify the input values or assert tests as needed.

## Improved Version (Object-Oriented)

```
package_robot/
├── robot.py       # Uses the sort() function with the Package class internally
├── package.py     # Package class with input validation and classification logic
├── test.py        # Assert-based test cases for multiple scenarios
└── README.md      # This file
```

### Usage
1. Run `python robot.py`.
2. Execute tests with `python test.py`

### Validations
The improved version includes input validation to handle edge cases:
- None values.
- Non-numeric values.
- Negative numbers.
