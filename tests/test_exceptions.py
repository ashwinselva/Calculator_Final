"""Tests for custom exceptions."""
import pytest
from app.exceptions import (
    CalculatorException,
    InvalidInputError,
    InvalidOperationError,
    DivisionByZeroError,
    InvalidRootError,
    OperationError
)


class TestExceptions:
    """Test suite for custom exceptions."""
    
    def test_calculator_exception_base(self):
        """Test base CalculatorException."""
        exc = CalculatorException("Test error")
        assert str(exc) == "Test error"
        assert isinstance(exc, Exception)
    
    def test_invalid_input_error(self):
        """Test InvalidInputError."""
        exc = InvalidInputError("Invalid input")
        assert isinstance(exc, CalculatorException)
        assert str(exc) == "Invalid input"
    
    def test_invalid_operation_error(self):
        """Test InvalidOperationError."""
        exc = InvalidOperationError("Invalid operation")
        assert isinstance(exc, CalculatorException)
        assert str(exc) == "Invalid operation"
    
    def test_division_by_zero_error(self):
        """Test DivisionByZeroError."""
        exc = DivisionByZeroError("Cannot divide by zero")
        assert isinstance(exc, CalculatorException)
        assert str(exc) == "Cannot divide by zero"
    
    def test_invalid_root_error(self):
        """Test InvalidRootError."""
        exc = InvalidRootError("Cannot take even root of negative")
        assert isinstance(exc, CalculatorException)
        assert str(exc) == "Cannot take even root of negative"
    
    def test_operation_error(self):
        """Test OperationError."""
        exc = OperationError("Operation failed")
        assert isinstance(exc, CalculatorException)
        assert str(exc) == "Operation failed"
    
    def test_exception_inheritance(self):
        """Test exception inheritance chain."""
        exc = InvalidInputError("Test")
        assert isinstance(exc, CalculatorException)
        assert isinstance(exc, Exception)
