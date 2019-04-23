## @package CChanMathlib
# Mathematical library for Calc-chan calculator.
#

##
# @brief Class representing the Calc-chan math library.
#
class CChanMathlib:

    ##
    # @brief Computes the sum of two numbers.
    #
    # @param a Summand
    # @param b Addend
    #
    # @return Sum of a and b
    #
    @staticmethod
    def add(a, b):
        return a + b

    ##
    # @brief Computes the difference of two numbers.
    #
    # @param a Minuend
    # @param b Subtrahend
    #
    # @return Difference of a and b
    #
    @staticmethod
    def sub(a, b):
        return a - b

    ##
    # @brief Computes the product of two numbers.
    #
    # @param a Multiplicand
    # @param b Multiplier
    #
    # @return Product of a and b
    #
    @staticmethod
    def mul(a, b):
        return a * b

    ##
    # @brief Computes the quotient from two numbers.
    #
    # @param a Dividend
    # @param b Divisor
    #
    # @return Quotient of a and b
    #
    # @exception ZeroDivisionError If a divisor is zero, the function raises ZeroDivisionError.
    #
    @staticmethod
    def div(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

    ##
    # @brief Computes the factorial of number.
    #
    # @param a Positive integer
    #
    # @return Factorial of a
    #
    # @exception ValueError If a negative or real number, the function raises ValueError.
    #
    @staticmethod
    def fact(a):
        if type(a) != int:
            raise ValueError("Factorial of real number.")
        elif a < 0:
            raise ValueError("Factorial of negative value.")
        elif a == 0:
            return 1
        else:
            res = 1
            while a > 0:
                res *= a
                a -= 1
            return res

    ##
    # @brief Computes base to the power of exponent.
    #
    # @param a Base
    # @param exp Exponent
    #
    # @return a to the power of exp
    #
    # @exception ValueError If the exponent is negative or a real number, the function raises ValueError.
    #
    @staticmethod
    def pow(a, exp):
        if type(exp) != int:
            raise ValueError("Exponent is not integer.")
        elif exp < 0:
            raise ValueError("Exponent is negative value.")
        elif exp == 0:
            return 1
        else:
            return a ** exp

    ##
    # @brief Computes n-th root of a number
    #
    # @param a Base
    # @param n Order of root
    #
    # @return n-th root of a
    #
    # @exception ValueError If the base value is negative or zero, the function raises ValueError.
    # If the order of root is negative or zero, the function also raises ValueError.
    #
    @staticmethod
    def root(a, n):
        if a < 0:
            raise ValueError("Order of root is zero or negative.")
        elif n <= 0:
            raise ValueError("Base value is negative or zero.")
        else:
            return a ** (1 / n)

    ##
    # @brief Computes natural logarithm a number.
    #
    # @param a Positive real number
    #
    # @return natural logarithm of a
    #
    # @exception ValueError If the number is negative or zero, the function raises ValueError.
    #
    @staticmethod
    def ln(a):
        if a <= 0:
            raise ValueError("Natural logarithm argument is zero or negative.")
        elif a == 1:
            return 0
        else:
            n = 10000000000.0
            return n * ((a ** (1/n)) - 1)
