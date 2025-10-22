import unittest
import io
import sys
from main import main


class TestMain(unittest.TestCase):
    """Test cases for the main module after refactoring to use Calculator"""

    def setUp(self):
        """Set up test fixtures - capture stdout"""
        self.captured_output = io.StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.captured_output

    def tearDown(self):
        """Tear down test fixtures - restore stdout"""
        sys.stdout = self.original_stdout

    def test_main_prints_hello(self):
        """Test that main() still prints the original hello message"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("Hello from hw2!", output)

    def test_main_prints_calculator_title(self):
        """Test that main() prints calculator title after refactoring"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("Interactive Calculator", output)

    def test_main_demonstrates_addition(self):
        """Test that main() demonstrates addition operation"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("2 + 3 = 5", output)

    def test_main_demonstrates_subtraction(self):
        """Test that main() demonstrates subtraction operation"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("5 - 3 = 2", output)

    def test_main_demonstrates_multiplication(self):
        """Test that main() demonstrates multiplication operation"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("4 * 3 = 12", output)

    def test_main_demonstrates_division(self):
        """Test that main() demonstrates division operation"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("10 / 2 = 5.0", output)

    def test_main_demonstrates_division_with_remainder(self):
        """Test that main() demonstrates division with decimal result"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("7 / 2 = 3.5", output)

    def test_main_prints_completion_message(self):
        """Test that main() prints completion message"""
        main()
        output = self.captured_output.getvalue()
        self.assertIn("All operations completed successfully!", output)

    def test_main_uses_calculator_class(self):
        """Test that main() integrates with Calculator class by checking all operations"""
        main()
        output = self.captured_output.getvalue()

        # Verify all four basic operations are demonstrated
        self.assertIn("2 + 3 = 5", output, "Addition not demonstrated")
        self.assertIn("5 - 3 = 2", output, "Subtraction not demonstrated")
        self.assertIn("4 * 3 = 12", output, "Multiplication not demonstrated")
        self.assertIn("10 / 2 = 5.0", output, "Division not demonstrated")


if __name__ == "__main__":
    unittest.main()
