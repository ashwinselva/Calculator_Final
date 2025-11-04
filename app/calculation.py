from . import history, logger
from .operations import Operations
from .input_validators import is_number
from .exceptions import (
    InvalidInputError, InvalidOperationError, 
    DivisionByZeroError, InvalidRootError, OperationError
)

# def show_help() -> None:
#     print("\nHelp - Available commands:")
#     print("1: Perform a calculation (you will be prompted for numbers and an operation)")
#     print("2: Show this help message")
#     print("3: Show calculation history")
#     print("4 or q: Exit the program")


# def show_history(calc: Calculator) -> None:
#     if not getattr(calc, "history", None):
#         print("\nNo history available.")
#         return
#     print("\nCalculation history:")
#     for i, entry in enumerate(calc.history, start=1):
#         print(f"{i}. {entry}")

def perform_operation() -> None:
    try:
        a_input = input("Enter the first number (a): ")
        if not is_number(a_input):
            raise InvalidInputError("Invalid input for the first number. Please enter a valid number.")
        a = float(a_input)
        
        b_input = input("Enter the second number (b): ")
        if not is_number(b_input):
            raise InvalidInputError("Invalid input for the second number. Please enter a valid number.")
        b = float(b_input)
        
        print("\nSelect operation:")
        print("1) Addition (a + b)")
        print("2) Subtraction (a - b)")
        print("3) Multiplication (a * b)")
        print("4) Division (a / b)")
        print("5) Power (a ** b)")
        print("6) Root (b-th root of a)")
        print("7) Modulus (a % b)")
        print("8) Integer Division (a // b)")
        print("9) Percentage (a% of b)")
        print("10) Absolute Difference |a - b|")
        
        try:
            op_choice = int(input("Choose operation (1-10): "))
        except ValueError:
            raise InvalidOperationError("Operation choice must be an integer between 1 and 10.")
        
        if op_choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            raise InvalidOperationError(f"Invalid operation choice: {op_choice}. Please choose between 1 and 10.")
        
        # Operation names mapping
        operation_names = {
            1: "Addition", 2: "Subtraction", 3: "Multiplication", 4: "Division",
            5: "Power", 6: "Root", 7: "Modulus", 8: "Integer Division",
            9: "Percentage", 10: "Absolute Difference"
        }
        
        ops = Operations()
        
        try:
            result = ops.operations[op_choice](a, b)
        except ZeroDivisionError as e:
            raise DivisionByZeroError(f"Cannot divide by zero. Error: {e}")
        except ValueError as e:
            raise InvalidRootError(f"Cannot take even root of negative number. Error: {e}")
        except Exception as e:
            raise OperationError(f"An error occurred during the operation: {e}")
        
        history.add_entry(a, b, result)
        
        # Log the operation
        operation_name = operation_names.get(op_choice, "Unknown")
        logger.log(a, b, operation_name, result)
        
        print(f"Result: {result}")
        
    except InvalidInputError as e:
        print(f"Input Error: {e}")
    except InvalidOperationError as e:
        print(f"Operation Error: {e}")
    except DivisionByZeroError as e:
        print(f"Math Error: {e}")
    except InvalidRootError as e:
        print(f"Math Error: {e}")
    except OperationError as e:
        print(f"Calculation Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


