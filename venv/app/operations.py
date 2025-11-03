"""Basic arithmetic operations mapping."""
from typing import Callable, Dict


class Operations:
    def __init__(self, options=None, a=None, b=None):
        self.operations: Dict[int, Callable[[float, float], float]] = {
            1: self.add,
            2: self.sub,
            3: self.mul,
            4: self.div,
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

        
        