"""Tests for the calculator operations."""
import pytest
from app.operations import Operations


class TestOperations:
    """Test suite for calculator operations."""
    
    @pytest.fixture
    def ops(self):
        """Create an operations instance for testing."""
        return Operations()
    
    def test_add(self, ops):
        """Test addition operation."""
        assert ops.add(5, 3) == 8
        assert ops.add(-5, 3) == -2
        assert ops.add(0, 0) == 0
        assert ops.add(5.5, 2.5) == 8.0
    
    def test_sub(self, ops):
        """Test subtraction operation."""
        assert ops.sub(5, 3) == 2
        assert ops.sub(-5, 3) == -8
        assert ops.sub(0, 0) == 0
        assert ops.sub(5.5, 2.5) == 3.0
    
    def test_mul(self, ops):
        """Test multiplication operation."""
        assert ops.mul(5, 3) == 15
        assert ops.mul(-5, 3) == -15
        assert ops.mul(0, 100) == 0
        assert ops.mul(5.5, 2) == 11.0
    
    def test_div(self, ops):
        """Test division operation."""
        assert ops.div(6, 3) == 2
        assert ops.div(10, 2) == 5
        assert ops.div(-10, 2) == -5
        assert ops.div(7, 2) == 3.5
    
    def test_div_by_zero(self, ops):
        """Test division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            ops.div(5, 0)
    
    def test_pow(self, ops):
        """Test power operation."""
        assert ops.pow(2, 3) == 8
        assert ops.pow(5, 2) == 25
        assert ops.pow(2, 0) == 1
        assert ops.pow(3, -1) == pytest.approx(1/3)
    
    def test_root(self, ops):
        """Test root operation."""
        assert ops.root(8, 3) == 2
        assert ops.root(16, 2) == 4
        assert ops.root(27, 3) == 3
    
    def test_root_negative_even(self, ops):
        """Test that even root of negative raises error."""
        with pytest.raises(ValueError):
            ops.root(-4, 2)
    
    def test_mod(self, ops):
        """Test modulus operation."""
        assert ops.mod(10, 3) == 1
        assert ops.mod(7, 2) == 1
        assert ops.mod(5, 5) == 0
    
    def test_mod_by_zero(self, ops):
        """Test modulus by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            ops.mod(5, 0)
    
    def test_integer_div(self, ops):
        """Test integer division operation."""
        assert ops.integer_div(10, 3) == 3
        assert ops.integer_div(7, 2) == 3
        assert ops.integer_div(15, 5) == 3
    
    def test_integer_div_by_zero(self, ops):
        """Test integer division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            ops.integer_div(5, 0)
    
    def test_percent(self, ops):
        """Test percentage operation."""
        assert ops.percent(50, 100) == 50  # 50% of 100
        assert ops.percent(25, 200) == 50  # 25% of 200
        assert ops.percent(10, 1000) == 100  # 10% of 1000
    
    def test_absolute_difference(self, ops):
        """Test absolute difference operation."""
        assert ops.absolute_difference(5, 3) == 2
        assert ops.absolute_difference(3, 5) == 2
        assert ops.absolute_difference(-5, 3) == 8
        assert ops.absolute_difference(0, 0) == 0
