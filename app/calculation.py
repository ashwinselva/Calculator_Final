from . import history, logger
from .operations import Operations
from .input_validators import is_number

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
    
    a_input = input("Enter the first number (a): ")
    if not is_number(a_input):
        print("Invalid input for the first number.")
        return
    a = float(a_input)
    
    b_input = input("Enter the second number (b): ")
    if not is_number(b_input):
        print("Invalid input for the second number.")
        return
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
    op_choice = int(input("Choose operation (1-10): "))
    ops = Operations()
    if op_choice not in [1,2,3,4,5,6,7,8,9,10]:
        print("Invalid operation choice.")
        return
    
    # Operation names mapping
    operation_names = {
        1: "Addition", 2: "Subtraction", 3: "Multiplication", 4: "Division",
        5: "Power", 6: "Root", 7: "Modulus", 8: "Integer Division",
        9: "Percentage", 10: "Absolute Difference"
    }
    
    result = ops.operations[op_choice](a, b)
    history.add_entry(a, b, result)
    
    # Log the operation
    operation_name = operation_names.get(op_choice, "Unknown")
    logger.log(a, b, operation_name, result)
    
    print(f"Result: {result}")


