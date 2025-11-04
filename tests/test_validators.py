"""Tests for input validators."""
import pytest
from app.input_validators import is_number


class TestInputValidators:
    """Test suite for input validators."""
    
    def test_is_number_with_integer_string(self):
        """Test is_number with integer string."""
        assert is_number("5") is True
        assert is_number("0") is True
        assert is_number("-10") is True
    
    def test_is_number_with_float_string(self):
        """Test is_number with float string."""
        assert is_number("5.5") is True
        assert is_number("0.0") is True
        assert is_number("-10.5") is True
    
    def test_is_number_with_integer(self):
        """Test is_number with integer."""
        assert is_number(5) is True
        assert is_number(0) is True
        assert is_number(-10) is True
    
    def test_is_number_with_float(self):
        """Test is_number with float."""
        assert is_number(5.5) is True
        assert is_number(0.0) is True
        assert is_number(-10.5) is True
    
    def test_is_number_with_invalid_string(self):
        """Test is_number with invalid string."""
        assert is_number("abc") is False
        assert is_number("5a") is False
        assert is_number("") is False
    
    def test_is_number_with_none(self):
        """Test is_number with None."""
        assert is_number(None) is False
    
    def test_is_number_with_special_values(self):
        """Test is_number with special float values."""
        assert is_number(float('inf')) is True
        assert is_number(float('-inf')) is True
        assert is_number(float('nan')) is True
