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

## Dependencies

- pytest >= 7.0
- pytest-cov >= 4.0.0
- coverage >= 7.0
- pandas >= 2.0.0
- colorama >= 0.4.6
