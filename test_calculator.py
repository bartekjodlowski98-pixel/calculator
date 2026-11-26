import pytest
from calculator import Calculator



class TestCalculator():
    def test_sum(self):
     calculator = Calculator(1, 2)
     assert calculator.sum() == 3





