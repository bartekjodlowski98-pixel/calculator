class Calculator:
    def __init__(self, op1: float, op2: float):
       self.op1 = op1
       self.op2 = op2

    def sum(self):
        return self.op1 + self.op2

    def subtract(self):
        return self.op1 - self.op2

    def multiply(self):
        return self.op1 * self.op2

    def divide(self):
        if self.op2 == 0:
            raise ZeroDivisionError("Division by 0")
        return self.op1 / self.op2

if __name__ == "__main__":
    calculator = Calculator(8.0, 4.0)
    calculator2 = Calculator(5.0, 0.0)
    print("sum:", calculator.sum(), calculator2.sum())
    print("subtract:", calculator.subtract(), calculator2.subtract())
    print("multiply:", calculator.multiply(),calculator2.multiply())
    print("divide:", calculator.divide(), calculator2.divide())