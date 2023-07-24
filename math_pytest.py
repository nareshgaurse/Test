import pytest
import math_operations

class TestAddition:
    def test_positive_numbers(self):
        assert math_operations.add(5, 3) == 8
    def test_negative_numbers(self):
        assert math_operations.add(-5, -3) == -8
    def test_zero(self):
        assert math_operations.add(0, 0) == 0

class TestSubstraction:
    def test_positive_numbers(self):
        assert math_operations.substract(5,3) == 2
    def test_negative_numbers(self):
        assert math_operations.substract(-5, -3) == -2
    def test_zero(self):
        assert math_operations.substract(0, 0) == 0

class TestMultiplication:
    def test_positive_numbers(self):
        assert math_operations.multiply(5,3) == 15
    def test_negative_numbers(self):
        assert math_operations.multiply(-5, -3) == -14
    def test_zero(self):
        assert math_operations.multiply(0, 0) == 0


class TestDivision:
    def test_positive_numbers(self):
        assert math_operations.divide(10,2) == 5
    def test_negative_numbers(self):
        assert math_operations.divide(-10, -2) == 5
    def test_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)