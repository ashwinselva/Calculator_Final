"""Custom exceptions for the calculator application."""


class CalculatorException(Exception):
    """Base exception class for calculator operations."""
    pass


class InvalidInputError(CalculatorException):
    """Raised when user input is invalid."""
    pass


class InvalidOperationError(CalculatorException):
    """Raised when an invalid operation is selected."""
    pass


class DivisionByZeroError(CalculatorException):
    """Raised when attempting to divide by zero."""
    pass


class InvalidRootError(CalculatorException):
    """Raised when attempting to take an even root of a negative number."""
    pass


class OperationError(CalculatorException):
    """Raised when an operation fails to execute."""
    pass
