import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)  # Expect 5 - 3 = 2

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)  # Expect 4 * 3 = 12

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5.0)  # Expect 10 / 2 = 5.0

    def test_divide_with_remainder(self):
        calc = Calculator()
        result = calc.divide(7, 2)
        self.assertAlmostEqual(result, 3.5)  # Expect 7 / 2 = 3.5

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(10, 0)  # Expect division by zero to raise ValueError

    def test_intentional_failure(self):
        """This test intentionally fails to demonstrate CI failure detection"""
        calc = Calculator()
        # This assertion is intentionally wrong to break the build
        self.assertEqual(calc.add(2, 2), 5, "Intentional failure: 2 + 2 should be 4, not 5")

if __name__ == "__main__":
    unittest.main()