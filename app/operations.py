"""Basic arithmetic operations mapping."""
from typing import Callable, Dict


class Operations:
    def __init__(self, options=None, a=None, b=None):
        self.operations: Dict[int, Callable[[float, float], float]] = {
            1: self.add,
            2: self.sub,
            3: self.mul,
            4: self.div,
            5: self.pow,
            6: self.root,
            7: self.mod,
            8: self.integer_div,
            9: self.percent,
            10: self.absolute_difference
        }
        self.a = a
        self.b = b

    def add(self, a: float, b: float) -> float:
        return a + b

    def sub(self, a: float, b: float) -> float:
        return a - b

    def mul(self, a: float, b: float) -> float:
        return a * b

    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    
    def pow(self, a: float, b: float) -> float:
        return a ** b
    
    def root(self, a: float, b: float) -> float:
        if a < 0 and b % 2 == 0:
            raise ValueError("cannot take even root of negative number")
        return a ** (1 / b)
    def mod(self, a: float, b: float) -> float:
        return a % b
    def integer_div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("integer division by zero")
        return a // b
    def percent(self, a: float, b: float) -> float:
        return (a / 100) * b
    def absolute_difference(self, a: float, b: float) -> float:
        return abs(a - b)



        
