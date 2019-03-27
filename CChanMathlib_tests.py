# Tests for mathematical library functions used for TDD.
# Run using: "python3 -m unittest CChanMathlib_tests.py"

import unittest
from CChanMathlib import CChanMathlib

if __name__ == '__main__':
    unittest.main()

# Tests for the addition function
class CChanTestAddition(unittest.TestCase):

    def test_addition_positive_integer(self):
        self.assertEqual(CChanMathlib.add(0, 0), 0)
        self.assertEqual(CChanMathlib.add(0, 5), 5)
        self.assertEqual(CChanMathlib.add(5, 0), 5)
        self.assertEqual(CChanMathlib.add(1, 1), 2)
        self.assertEqual(CChanMathlib.add(12345, 54321), 66666)

    def test_addition_negative_integer(self):
        self.assertEqual(CChanMathlib.add(-1, 0), -1)
        self.assertEqual(CChanMathlib.add(0, -1), -1)
        self.assertEqual(CChanMathlib.add(-1, -1), -2)
        self.assertEqual(CChanMathlib.add(-12345, -54321), -66666)

    def test_addition_mixed_integer(self):
        self.assertEqual(CChanMathlib.add(-1, 1), 0)
        self.assertEqual(CChanMathlib.add(1, -2), -1)
        self.assertEqual(CChanMathlib.add(2, -1), 1)

    def test_addition_positive_float(self):
        self.assertEqual(CChanMathlib.add(0.0, 0.0), 0.0)
        self.assertEqual(CChanMathlib.add(0.5, 0.0), 0.5)
        self.assertEqual(CChanMathlib.add(0.0, 0.5), 0.5)
        self.assertEqual(CChanMathlib.add(17.3, 48.5), 65.8)

    def test_addition_negative_float(self):
        self.assertEqual(CChanMathlib.add(-0.1, 0.0), -0.1)
        self.assertEqual(CChanMathlib.add(0.0, -0.1), -0.1)
        self.assertEqual(CChanMathlib.add(-0.5, -0.5), -1.0)
        self.assertEqual(CChanMathlib.add(-17.3, -48.5), -65.8)

    def test_addition_mixed_float(self):
        self.assertEqual(CChanMathlib.add(-1.0, 1.0), 0.0)
        self.assertEqual(CChanMathlib.add(1.3, -2.7), -1.4)
        self.assertEqual(CChanMathlib.add(2.7, -1.3), 1.4)

# Tests for the subtraction function
class CChanTestSubtraction(unittest.TestCase):

    def test_subtraction_positive_integer(self):
        self.assertEqual(CChanMathlib.sub(0, 0), 0)
        self.assertEqual(CChanMathlib.sub(0, 5), -5)
        self.assertEqual(CChanMathlib.sub(5, 0), 5)
        self.assertEqual(CChanMathlib.sub(10, 5), 5)
        self.assertEqual(CChanMathlib.sub(5, 10), -5)
        self.assertEqual(CChanMathlib.sub(66666, 54321), 12345)

    def test_subtraction_negative_integer(self):
        self.assertEqual(CChanMathlib.sub(-5, 0), -5)
        self.assertEqual(CChanMathlib.sub(0, -5), 5)
        self.assertEqual(CChanMathlib.sub(-5, -10), 5)
        self.assertEqual(CChanMathlib.sub(-10, -5), -5)

    def test_subtraction_mixed_integer(self):
        self.assertEqual(CChanMathlib.sub(-1, 1), -2)
        self.assertEqual(CChanMathlib.sub(1, -1), 2)
        self.assertEqual(CChanMathlib.sub(10, -5), 15)

    def test_subtraction_positive_float(self):
        self.assertEqual(CChanMathlib.sub(0.0, 0.0), 0.0)
        self.assertEqual(CChanMathlib.sub(0.5, 0.0), 0.5)
        self.assertEqual(CChanMathlib.sub(0.0, 0.5), -0.5)
        self.assertEqual(CChanMathlib.sub(65.8, 48.5), 17.3)

    def test_subtraction_negative_float(self):
        self.assertEqual(CChanMathlib.sub(-0.1, 0.0), -0.1)
        self.assertEqual(CChanMathlib.sub(0.0, -0.1), 0.1)
        self.assertEqual(CChanMathlib.sub(-0.5, -0.5), 0)
        self.assertEqual(CChanMathlib.sub(-65.8, -48.5), -17.3)

    def test_subtraction_mixed_float(self):
        self.assertEqual(CChanMathlib.sub(0.1, -0.1), 0.2)
        self.assertEqual(CChanMathlib.sub(-0.1, 0.1), -0.2)
        self.assertEqual(CChanMathlib.sub(2.7, -1.3), 4.0)