# Calculator.py to do mathematical operations
class Calculator:
    # Addition
    def add(self, a, b):
        return a + b

    # Subtraction
    def sub(self, a, b):
        return a - b

    # Multiplication 
    def mul(self, a, b):
        return a * b

    # Division
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return ("Number can't be divided by zero.")
