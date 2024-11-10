import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_positive(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-6, 2), -3)

    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-10, 3), -1)

if __name__ == '__main__':
    unittest.main()
