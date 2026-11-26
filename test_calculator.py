import pytest
from calculator import Calculator



class TestCalculator():
    def test_sum(self):
        calculator = Calculator(1.0, 2.0)
        assert calculator.sum() == 3.0
        calculator = Calculator(2.0, 3.5)
        assert calculator.sum() == 5.5
        calculator = Calculator(3.5, 4.5)
        assert calculator.sum() == 8.0
        calculator = Calculator(4.0, -5.0)
        assert calculator.sum() == -1.0

    def test_subtract(self):
        calculator = Calculator(3.0, 2.0)
        assert calculator.subtract() == 1.0
        calculator = Calculator(5.5, 3.0)
        assert calculator.subtract() == 2.5
        calculator = Calculator(7.5, 4.0)
        assert calculator.subtract() == 3.5
        calculator = Calculator(5.0, 9.0)
        assert calculator.subtract() == -4.0

    def test_multiply(self):
        calculator = Calculator(2.0, 3.0)
        assert calculator.multiply() == 6.0
        calculator = Calculator(2.5, 4.0)
        assert calculator.multiply() == 10.0
        calculator = Calculator(2.0, -5.5)
        assert calculator.multiply() == -11.0
        calculator = Calculator(2.0, 0.0)
        assert calculator.multiply() == 0.0

    def test_divide(self):
        calculator = Calculator(4.0, 2.0)
        assert calculator.divide() == 2.0
        calculator = Calculator(5.0, 2.0)
        assert calculator.divide() == 2.5
        calculator = Calculator(9.0, -2)
        assert calculator.divide() == -4.5
        calculator = Calculator(4.0, 0.0)
        with pytest.raises(ZeroDivisionError):
            calculator.divide()
