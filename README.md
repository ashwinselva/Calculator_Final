# Calculator Application

A simple Python calculator with persistent history, file-based logging, and color-coded output.

## Features

- 10 arithmetic operations (Addition, Subtraction, Multiplication, Division, Power, Root, Modulus, Integer Division, Percentage, Absolute Difference)
- Persistent calculation history saved to CSV
- Timestamped operation logging
- Color-coded console output
- Custom exception handling
- Input validation

## How to Run

### Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the Calculator

```bash
python run_calculator.py
```

### Run Tests

```bash
python -m pytest tests/ -v
```

### Run Tests with Coverage

```bash
python -m pytest tests/ --cov=app --cov-report=term-missing
```

## Project Structure

```
app/
├── calculator.py          # Main menu and program loop
├── calculation.py         # Operation orchestration
├── operations.py          # 10 arithmetic operations
├── history.py             # Calculation history management
├── logger.py              # Operation logging
├── colors.py              # Color utilities
├── exceptions.py          # Custom exceptions
├── help.py                # Menu display
├── input_validators.py    # Input validation
└── history.csv            # Persistent history file

tests/
├── test_operations.py     # Operation tests
├── test_validators.py     # Validator tests
├── test_exceptions.py     # Exception tests
├── test_history.py        # History tests
└── test_integration.py    # Integration tests
```

## Menu Options

1. Perform calculation
2. Help
3. View history
4. Clear history
5. Clear last entry
6. Redo last entry
7. Save history
8. Load history
9. Exit

## Output Examples

### Main Menu
```
============================================================
                     Simple Calculator                      
============================================================

ℹ Type a menu number to interact. Type '9' or 'q' to quit.

Menu:
1) Perform calculation
2) Help
3) History
4) Clear History
5) Clear Last Entry
6) Redo Last Entry
7) Save History
8) Load History
9) Exit
ℹ Choose a number: 
```

### Calculation Flow
```
ℹ Enter the first number (a): 10
ℹ Enter the second number (b): 5

ℹ 
Select operation:
1) Addition (a + b)
2) Subtraction (a - b)
3) Multiplication (a * b)
4) Division (a / b)
5) Power (a ** b)
6) Root (b-th root of a)
7) Modulus (a % b)
8) Integer Division (a // b)
9) Percentage (a% of b)
10) Absolute Difference |a - b|
ℹ Choose operation (1-10): 1

[2025-11-03 22:23:04] LOG: Performed Addition on 10.0 and 5.0 with result 15.0
✓ Result: 15.0
```

### History Display
```
ℹ 
Calculation history:
  a         b         Result
──────────────────────────────
  10.00     5.00         15.00
  20.00     4.00          5.00
  50.00     2.00          25.00
```

### Success Messages
```
✓ History cleared.
✓ Loaded 3 entries from history
✓ Goodbye!
```

### Error Messages
```
✗ Input Error: Invalid input for the first number. Please enter a valid number.
✗ Operation Error: Invalid operation choice: 15. Please choose between 1 and 10.
✗ Math Error: Cannot divide by zero. Error: division by zero
```

## Test Coverage

- **Total Coverage**: 92.93%
- **Tests Passing**: 92/92 ✅
- **100% Coverage Modules**: operations.py, exceptions.py, input_validators.py, colors.py, help.py, __init__.py

## Dependencies

- pytest >= 7.0
- pytest-cov >= 4.0.0
- coverage >= 7.0
- pandas >= 2.0.0
- colorama >= 0.4.6
