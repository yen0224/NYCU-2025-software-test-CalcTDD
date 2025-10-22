import math


class Calculator:
    def add(self, a, b):
        result = a + b
        if math.isinf(result):
            raise OverflowError(f"Addition overflow: {a} + {b} exceeds float limits")
        return result

    def subtract(self, a, b):
        result = a - b
        if math.isinf(result):
            raise OverflowError(f"Subtraction overflow: {a} - {b} exceeds float limits")
        return result

    def multiply(self, a, b):
        result = a * b
        if math.isinf(result):
            raise OverflowError(f"Multiplication overflow: {a} * {b} exceeds float limits")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        if math.isinf(result):
            raise OverflowError(f"Division overflow: {a} / {b} exceeds float limits")
        return result