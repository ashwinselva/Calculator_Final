from . import history, logger
from .operations import Operations
from .input_validators import is_number
from .colors import print_info, print_success, print_error, print_warning, Colors, highlight
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
        a_input = input(f"{Colors.INFO}Enter the first number (a): {Colors.RESET}")
        if not is_number(a_input):
            raise InvalidInputError("Invalid input for the first number. Please enter a valid number.")
        a = float(a_input)
        
        b_input = input(f"{Colors.INFO}Enter the second number (b): {Colors.RESET}")
        if not is_number(b_input):
            raise InvalidInputError("Invalid input for the second number. Please enter a valid number.")
        b = float(b_input)
        
        print_info("\nSelect operation:")
        print(f"{Colors.SUCCESS}1){Colors.RESET} Addition (a + b)")
        print(f"{Colors.SUCCESS}2){Colors.RESET} Subtraction (a - b)")
        print(f"{Colors.SUCCESS}3){Colors.RESET} Multiplication (a * b)")
        print(f"{Colors.SUCCESS}4){Colors.RESET} Division (a / b)")
        print(f"{Colors.SUCCESS}5){Colors.RESET} Power (a ** b)")
        print(f"{Colors.SUCCESS}6){Colors.RESET} Root (b-th root of a)")
        print(f"{Colors.SUCCESS}7){Colors.RESET} Modulus (a % b)")
        print(f"{Colors.SUCCESS}8){Colors.RESET} Integer Division (a // b)")
        print(f"{Colors.SUCCESS}9){Colors.RESET} Percentage (a% of b)")
        print(f"{Colors.SUCCESS}10){Colors.RESET} Absolute Difference |a - b|")
        
        try:
            op_choice = int(input(f"{Colors.INFO}Choose operation (1-10): {Colors.RESET}"))
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
        
        print_success(f"Result: {highlight(str(result))}")
        
    except InvalidInputError as e:
        print_error(f"Input Error: {e}")
    except InvalidOperationError as e:
        print_error(f"Operation Error: {e}")
    except DivisionByZeroError as e:
        print_error(f"Math Error: {e}")
    except InvalidRootError as e:
        print_error(f"Math Error: {e}")
    except OperationError as e:
        print_error(f"Calculation Error: {e}")
    except Exception as e:
        print_error(f"Unexpected Error: {e}")


