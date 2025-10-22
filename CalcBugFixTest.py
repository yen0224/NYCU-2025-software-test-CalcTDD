import unittest
import math
from Calc import Calculator


class TestCalculatorOverflowBug(unittest.TestCase):
    """
    Test suite to capture and fix overflow bugs in Calculator.

    Bug Description:
    The Calculator class does not handle numeric overflow properly.
    When operations result in values exceeding float limits, Python
    returns 'inf' (infinity), which may not be the desired behavior
    in a calculator application.

    Expected Behavior:
    The calculator should raise an OverflowError when operations
    would result in infinity, alerting the user to the problem
    rather than silently returning inf.
    """

    def setUp(self):
        """Set up test fixtures"""
        self.calc = Calculator()

    # Tests that demonstrate the BUG (these will FAIL initially)

    def test_add_overflow_positive(self):
        """Test that adding very large numbers raises OverflowError"""
        # This test captures the bug: currently returns inf, should raise error
        with self.assertRaises(OverflowError):
            result = self.calc.add(1e308, 1e308)
            # If we get here without raising, the test fails

    def test_multiply_overflow(self):
        """Test that multiplying very large numbers raises OverflowError"""
        with self.assertRaises(OverflowError):
            result = self.calc.multiply(1e200, 1e200)

    def test_subtract_overflow_negative(self):
        """Test that subtracting to negative infinity raises OverflowError"""
        with self.assertRaises(OverflowError):
            result = self.calc.subtract(-1e308, 1e308)

    # Tests that should PASS (normal operations)

    def test_add_normal_numbers(self):
        """Test that normal addition still works"""
        result = self.calc.add(100, 200)
        self.assertEqual(result, 300)

    def test_add_large_but_safe_numbers(self):
        """Test that large but safe numbers work"""
        result = self.calc.add(1e100, 1e100)
        self.assertEqual(result, 2e100)
        self.assertFalse(math.isinf(result))

    def test_multiply_normal_numbers(self):
        """Test that normal multiplication still works"""
        result = self.calc.multiply(10, 20)
        self.assertEqual(result, 200)

    def test_divide_normal_numbers(self):
        """Test that normal division still works"""
        result = self.calc.divide(100, 2)
        self.assertEqual(result, 50.0)


if __name__ == "__main__":
    unittest.main()
