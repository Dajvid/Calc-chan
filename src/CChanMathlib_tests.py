# Tests for mathematical library functions used for TDD.
# Run using: "python3 -m unittest CChanMathlib_tests.py"

import unittest
from CChanMathlib import CChanMathlib
from CChanParser import CChanParser

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
        self.assertAlmostEqual(CChanMathlib.add(0.0, 0.0), 0.0)
        self.assertAlmostEqual(CChanMathlib.add(0.5, 0.0), 0.5)
        self.assertAlmostEqual(CChanMathlib.add(0.0, 0.5), 0.5)
        self.assertAlmostEqual(CChanMathlib.add(17.3, 48.5), 65.8)

    def test_addition_negative_float(self):
        self.assertAlmostEqual(CChanMathlib.add(-0.1, 0.0), -0.1)
        self.assertAlmostEqual(CChanMathlib.add(0.0, -0.1), -0.1)
        self.assertAlmostEqual(CChanMathlib.add(-0.5, -0.5), -1.0)
        self.assertAlmostEqual(CChanMathlib.add(-17.3, -48.5), -65.8)

    def test_addition_mixed_float(self):
        self.assertAlmostEqual(CChanMathlib.add(-1.0, 1.0), 0.0)
        self.assertAlmostEqual(CChanMathlib.add(1.3, -2.7), -1.4)
        self.assertAlmostEqual(CChanMathlib.add(2.7, -1.3), 1.4)


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
        self.assertAlmostEqual(CChanMathlib.sub(0.0, 0.0), 0.0)
        self.assertAlmostEqual(CChanMathlib.sub(0.5, 0.0), 0.5)
        self.assertAlmostEqual(CChanMathlib.sub(0.0, 0.5), -0.5)
        self.assertAlmostEqual(CChanMathlib.sub(65.8, 48.5), 17.3)

    def test_subtraction_negative_float(self):
        self.assertAlmostEqual(CChanMathlib.sub(-0.1, 0.0), -0.1)
        self.assertAlmostEqual(CChanMathlib.sub(0.0, -0.1), 0.1)
        self.assertAlmostEqual(CChanMathlib.sub(-0.5, -0.5), 0)
        self.assertAlmostEqual(CChanMathlib.sub(-65.8, -48.5), -17.3)

    def test_subtraction_mixed_float(self):
        self.assertAlmostEqual(CChanMathlib.sub(0.1, -0.1), 0.2)
        self.assertAlmostEqual(CChanMathlib.sub(-0.1, 0.1), -0.2)
        self.assertAlmostEqual(CChanMathlib.sub(2.7, -1.3), 4.0)


# Tests for the multiplication function
class CChanTestMultiplication(unittest.TestCase):

    def test_multiplication_positive_integer(self):
        self.assertEqual(CChanMathlib.mul(0, 0), 0)
        self.assertEqual(CChanMathlib.mul(0, 5), 0)
        self.assertEqual(CChanMathlib.mul(5, 0), 0)
        self.assertEqual(CChanMathlib.mul(5, 6), 30)
        self.assertEqual(CChanMathlib.mul(6, 5), 30)

    def test_multiplication_negative_integer(self):
        self.assertEqual(CChanMathlib.mul(-5, 0), 0)
        self.assertEqual(CChanMathlib.mul(0, -5), 0)
        self.assertEqual(CChanMathlib.mul(-5, -10), 50)
        self.assertEqual(CChanMathlib.mul(-10, -5), 50)

    def test_multiplication_mixed_integer(self):
        self.assertEqual(CChanMathlib.mul(-1, 1), -1)
        self.assertEqual(CChanMathlib.mul(1, -1), -1)
        self.assertEqual(CChanMathlib.mul(-10, 5), -50)

    def test_multiplication_positive_float(self):
        self.assertAlmostEqual(CChanMathlib.mul(0.0, 0.0), 0.0)
        self.assertAlmostEqual(CChanMathlib.mul(0.5, 0.0), 0.0)
        self.assertAlmostEqual(CChanMathlib.mul(0.0, 0.5), 0.0)
        self.assertAlmostEqual(CChanMathlib.mul(2.7, 1.35), 3.645)

    def test_multiplication_negative_float(self):
        self.assertAlmostEqual(CChanMathlib.mul(-0.1, 0.0), 0.0)
        self.assertAlmostEqual(CChanMathlib.mul(0.0, -0.1), 0.0)
        self.assertAlmostEqual(CChanMathlib.mul(-0.5, -0.5), 0.25)
        self.assertAlmostEqual(CChanMathlib.mul(-17.3, -48.55), 839.915)

    def test_multiplication_mixed_float(self):
        self.assertAlmostEqual(CChanMathlib.mul(0.1, -0.2), -0.02)
        self.assertAlmostEqual(CChanMathlib.mul(-0.1, 0.2), -0.02)
        self.assertAlmostEqual(CChanMathlib.mul(2.7, -1.3), -3.51)


# Tests for the division function
class CChanTestDivision(unittest.TestCase):

    def test_division_positive_integer(self):
        self.assertEqual(CChanMathlib.div(0, 1), 0)
        self.assertEqual(CChanMathlib.div(2, 1), 2.0)
        self.assertAlmostEqual(CChanMathlib.div(5, 2), 2.5)

    def test_division_negative_integer(self):
        self.assertEqual(CChanMathlib.div(0, -1), 0)
        self.assertEqual(CChanMathlib.div(-2, -1), 2)
        self.assertAlmostEqual(CChanMathlib.div(-5, -2), 2.5)

    def test_division_mixed_integer(self):
        self.assertEqual(CChanMathlib.div(-2, 1), -2)
        self.assertEqual(CChanMathlib.div(2, -1), -2)
        self.assertAlmostEqual(CChanMathlib.div(5, -2), -2.5)

    def test_division_positive_float(self):
        self.assertAlmostEqual(CChanMathlib.div(0.0, 0.5), 0.0)
        self.assertAlmostEqual(CChanMathlib.div(2.7, 1.3), 2.0769, 4)
        self.assertAlmostEqual(CChanMathlib.div(1.3, 2.7), 0.4815, 4)

    def test_division_negative_float(self):
        self.assertAlmostEqual(CChanMathlib.div(0.0, -0.5), 0.0)
        self.assertAlmostEqual(CChanMathlib.div(-2.7, -1.3), 2.0769, 4)
        self.assertAlmostEqual(CChanMathlib.div(-1.3, -2.7), 0.4815, 4)

    def test_division_mixed_float(self):
        self.assertAlmostEqual(CChanMathlib.div(0.1, -0.2), -0.5)
        self.assertAlmostEqual(CChanMathlib.div(-0.1, 0.2), -0.5)
        self.assertAlmostEqual(CChanMathlib.div(2.7, -1.3), -2.0769, 4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            CChanMathlib.div(10, 0)

        with self.assertRaises(ZeroDivisionError):
            CChanMathlib.div(10.0, 0)

        with self.assertRaises(ZeroDivisionError):
            CChanMathlib.div(10, 0.0)

        with self.assertRaises(ZeroDivisionError):
            CChanMathlib.div(10.0, 0.0)


# Tests for the factorial function
class CChanFactorialTest(unittest.TestCase):

    def test_factorial_positive_integer(self):
        self.assertEqual(CChanMathlib.fact(0), 1)
        self.assertEqual(CChanMathlib.fact(1), 1)
        self.assertEqual(CChanMathlib.fact(12), 479001600)

    def test_factorial_negative_integer(self):
        with self.assertRaises(ValueError):
            CChanMathlib.fact(0.5)

        with self.assertRaises(ValueError):
            CChanMathlib.fact(2.5)

        with self.assertRaises(ValueError):
            CChanMathlib.fact(-1)

        with self.assertRaises(ValueError):
            CChanMathlib.fact(-10)


# Tests for the power function
class CChanPowerTest(unittest.TestCase):

    def test_power_integer_base(self):
        self.assertEqual(CChanMathlib.pow(2, 0), 1)
        self.assertEqual(CChanMathlib.pow(2, 2), 4)
        self.assertEqual(CChanMathlib.pow(2, 5), 32)
        self.assertEqual(CChanMathlib.pow(-2, 0), 1)
        self.assertEqual(CChanMathlib.pow(-2, 2), 4)
        self.assertEqual(CChanMathlib.pow(-2, 5), -32)

    def test_power_float_base(self):
        self.assertAlmostEqual(CChanMathlib.pow(2.5, 0), 1.0)
        self.assertAlmostEqual(CChanMathlib.pow(2.5, 2), 6.25)
        self.assertAlmostEqual(CChanMathlib.pow(2.5, 5), 97.65625, 5)
        self.assertAlmostEqual(CChanMathlib.pow(-2.5, 0), 1.0)
        self.assertAlmostEqual(CChanMathlib.pow(-2.5, 2), 6.25)
        self.assertAlmostEqual(CChanMathlib.pow(-2.5, 5), -97.65625, 5)

    def test_power_invalid_exp(self):
        with self.assertRaises(ValueError):
            CChanMathlib.pow(2, -2)

        with self.assertRaises(ValueError):
            CChanMathlib.pow(2.5, -2)

        with self.assertRaises(ValueError):
            CChanMathlib.pow(2, 2.5)

        with self.assertRaises(ValueError):
            CChanMathlib.pow(2.5, 2.5)

        with self.assertRaises(ValueError):
            CChanMathlib.pow(2, -2.5)

        with self.assertRaises(ValueError):
            CChanMathlib.pow(2.5, -2.5)


# Tests for the root function
class CChanRootTest(unittest.TestCase):

    def test_root_positive_integer(self):
        self.assertEqual(CChanMathlib.root(0, 3), 0)
        self.assertEqual(CChanMathlib.root(25, 2), 5)
        self.assertEqual(CChanMathlib.root(81, 4), 3)
        self.assertAlmostEqual(CChanMathlib.root(125, 5), 2.6265, 4)

    def test_root_positive_float(self):
        self.assertEqual(CChanMathlib.root(5, 0.5), 25)
        self.assertAlmostEqual(CChanMathlib.root(10, 2.5), 2.5119, 4)
        self.assertAlmostEqual(CChanMathlib.root(125, 5.5), 2.4058, 4)

    def test_root_invalid(self):
        with self.assertRaises(ValueError):
            CChanMathlib.root(2, 0)

        with self.assertRaises(ValueError):
            CChanMathlib.root(-2, 0)

        with self.assertRaises(ValueError):
            CChanMathlib.root(-25, 2)

        with self.assertRaises(ValueError):
            CChanMathlib.root(25, -2)

        with self.assertRaises(ValueError):
            CChanMathlib.root(-25, -2)

        with self.assertRaises(ValueError):
            CChanMathlib.root(-125, 5.5)

        with self.assertRaises(ValueError):
            CChanMathlib.root(125, -5.5)

        with self.assertRaises(ValueError):
            CChanMathlib.root(-125, -5.5)


# Tests for the ln function
class CChanLnTest(unittest.TestCase):

    def test_ln_positive(self):
        self.assertEqual(CChanMathlib.ln(1), 0)
        self.assertAlmostEqual(CChanMathlib.ln(0.5), -0.693147, 6)
        self.assertAlmostEqual(CChanMathlib.ln(5), 1.609437, 6)
        self.assertAlmostEqual(CChanMathlib.ln(100), 4.605170, 6)

    def test_ln_invalid(self):
        with self.assertRaises(ValueError):
            CChanMathlib.ln(0)
        with self.assertRaises(ValueError):
            CChanMathlib.ln(-0.5)
        with self.assertRaises(ValueError):
            CChanMathlib.ln(-5)


# Tests for the eval function
class CChanEvalSimpleExpressionTest(unittest.TestCase):

    def test_eval_addition_expression(self):
        self.assertEqual(CChanParser.eval("0+5"), 5)
        self.assertEqual(CChanParser.eval("5+0"), 5)
        self.assertEqual(CChanParser.eval("15+17"), 32)
        self.assertEqual(CChanParser.eval("3+9"), 12)
        self.assertEqual(CChanParser.eval("3-9"), -6)
        self.assertEqual(CChanParser.eval("5-5"), 0)
        self.assertAlmostEqual(CChanParser.eval("4-2.7"), 1.3)
        self.assertAlmostEqual(CChanParser.eval("4-2.7"), 1.3)
        self.assertEqual(CChanParser.eval("2.7+1.3"), 4)

    def test_eval_subtraction_expression(self):
        self.assertEqual(CChanParser.eval("0-5"), -5)
        self.assertEqual(CChanParser.eval("5-0"), 5)
        self.assertEqual(CChanParser.eval("15-17"), -2)
        self.assertEqual(CChanParser.eval("-3-9"), -12)
        self.assertEqual(CChanParser.eval("3--9"), 12)
        self.assertEqual(CChanParser.eval("-5--5"), 0)
        self.assertAlmostEqual(CChanParser.eval("-2.7-4"), -6.7)
        self.assertAlmostEqual(CChanParser.eval("4--2.7"), 6.7)
        self.assertAlmostEqual(CChanParser.eval("2.7-1.3"), 1.4)

    def test_eval_multiplication_expression(self):
        self.assertEqual(CChanParser.eval("0*5"), 0)
        self.assertEqual(CChanParser.eval("5*0"), 0)
        self.assertEqual(CChanParser.eval("15*17"), 255)
        self.assertEqual(CChanParser.eval("-3*9"), -27)
        self.assertEqual(CChanParser.eval("3*-9"), -27)
        self.assertEqual(CChanParser.eval("-5*-5"), 25)
        self.assertAlmostEqual(CChanParser.eval("-2.7*4"), -10.8)
        self.assertAlmostEqual(CChanParser.eval("4*-2.7"), -10.8)
        self.assertAlmostEqual(CChanParser.eval("2.7*1.3"), 3.51)

    def test_eval_division_expression(self):
        self.assertAlmostEqual(CChanParser.eval("1/5"), 0.2)
        self.assertEqual(CChanParser.eval("5/1"), 5)
        self.assertAlmostEqual(CChanParser.eval("15/17"), 0.88235, 5)
        self.assertAlmostEqual(CChanParser.eval("-3/9"), -0.3333, 4)
        self.assertAlmostEqual(CChanParser.eval("3/-9"), -0.3333, 4)
        self.assertEqual(CChanParser.eval("-5/-5"), 1)
        self.assertAlmostEqual(CChanParser.eval("-2.7/4"), -0.675)
        self.assertAlmostEqual(CChanParser.eval("4/-2.7"), -1.48148, 4)
        self.assertAlmostEqual(CChanParser.eval("2.7/1.3"), 2.0769, 4)
        with self.assertRaises(ZeroDivisionError):
            CChanParser.eval("5/0")

    def test_eval_power_expression(self):
        self.assertEqual(CChanParser.eval("0^5"), 0)
        self.assertEqual(CChanParser.eval("5^0"), 1)
        self.assertEqual(CChanParser.eval("5^7"), 78125)
        self.assertEqual(CChanParser.eval("-3^9"), -19683)
        self.assertAlmostEqual(CChanParser.eval("-2.7^4"), -53.1441)
        with self.assertRaises(ValueError):
            CChanParser.eval("3^-9")
        with self.assertRaises(ValueError):
            CChanParser.eval("-5^-5")
        with self.assertRaises(ValueError):
            CChanParser.eval("4^-2.7")
        with self.assertRaises(ValueError):
            CChanParser.eval("2.7^1.3")

    def test_eval_root_expression(self):
        self.assertEqual(CChanParser.eval("3√0"), 0)
        self.assertEqual(CChanParser.eval("2√25"), 5)
        self.assertEqual(CChanParser.eval("4√81"), 3)
        self.assertAlmostEqual(CChanParser.eval("5√125"), 2.6265, 4)
        self.assertEqual(CChanParser.eval("0.5√5"), 25)
        self.assertAlmostEqual(CChanParser.eval("2.5√10"), 2.5119, 4)
        with self.assertRaises(ValueError):
            CChanParser.eval("0√2")
        with self.assertRaises(ValueError):
            CChanParser.eval("0√-2")
        with self.assertRaises(ValueError):
            CChanParser.eval("2√-25")
        with self.assertRaises(ValueError):
            CChanParser.eval("(-2)√25")
        with self.assertRaises(ValueError):
            CChanParser.eval("5.5√-125")
        with self.assertRaises(ValueError):
            CChanParser.eval("(-5.5)√125")
        with self.assertRaises(ValueError):
            CChanParser.eval("(-5.5)√-125")

    def test_eval_ln_expression(self):
        self.assertEqual(CChanParser.eval("ln(1)"), 0)
        self.assertAlmostEqual(CChanParser.eval("ln(0.5)"), -0.693147, 6)
        self.assertAlmostEqual(CChanParser.eval("ln(5)"), 1.609437, 6)
        self.assertAlmostEqual(CChanParser.eval("ln(100)"), 4.605170, 6)
        with self.assertRaises(ValueError):
            CChanParser.eval("ln(0)")
        with self.assertRaises(ValueError):
            CChanParser.eval("ln(-0.5)")
        with self.assertRaises(ValueError):
            CChanParser.eval("ln(-5)")

    def test_eval_simple_invalid_expression(self):
        with self.assertRaises(SyntaxError):
            CChanParser.eval("1+")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("+1")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("1++")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("-+1")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("1-")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("1*")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("*1")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("1/")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("/1")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("!")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("!1")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("1^")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("^1")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("^")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("5√")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("√")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("-√")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("ln")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("ln-")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("-ln")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("ln*5")


# Tests for the eval function using more complex expressions
class CChanEvalAdvancedExpressionTest(unittest.TestCase):

    def test_eval_advanced_expression(self):
        self.assertEqual(CChanParser.eval("5+4-3*2/1"), 3)
        self.assertEqual(CChanParser.eval("5!/120"), 1)
        self.assertEqual(CChanParser.eval("2√25*ln(1)"), 0)
        self.assertEqual(CChanParser.eval("5^2+14/2"), 32)
        self.assertEqual(CChanParser.eval("1734^ln(1)"), 1)
        self.assertAlmostEqual(CChanParser.eval("ln(10^2)"), 4.60517018, 5)
        self.assertAlmostEqual(CChanParser.eval("2√25/2+17^2"), 291.5)

    def test_eval_advanced_valueerror_expression(self):
        with self.assertRaises(ZeroDivisionError):
            CChanParser.eval("2√25/ln(1)")
        with self.assertRaises(ValueError):
            CChanParser.eval("5^ln(0.5)")
        with self.assertRaises(ValueError):
            CChanParser.eval("ln(0.5)√25")
        with self.assertRaises(ValueError):
            CChanParser.eval("5√ln(0.5)")
        with self.assertRaises(ValueError):
            CChanParser.eval("ln(0^5)")

    def test_eval_invalid_advanced_expression(self):
        with self.assertRaises(SyntaxError):
            CChanParser.eval("5+*4-2")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("ln-ln1")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("5!*+√25")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("5!+√*25")
        with self.assertRaises(SyntaxError):
            CChanParser.eval("123^ln1+!5")
