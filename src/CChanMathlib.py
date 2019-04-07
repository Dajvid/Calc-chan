# @package CChanMathlib
#  Mathematical library for CalcChan calculator.


class CChanMathlib:
    @staticmethod
    def add(a, b):
        ##
        # Addition function
        # Args:
        #     a: Addition argument.
        #     b: Addition argument.
        # Returns:
        #     Value of the following expression a+b.
        #
        return a + b

    @staticmethod
    def sub(a, b):
        ##
        # Subtraction function
        # Args:
        #     a: Subtraction argument.
        #     b: Subtraction argument.
        # Returns:
        #     Value of the following expression a-b.
        #
        return a - b

    @staticmethod
    def mul(a, b):
        ##
        # Multiplication function
        # Args:
        #     a: Multiplication argument.
        #     b: Multiplication argument.
        # Returns:
        #     Value of the following expression a*b.
        #
        return a * b

    @staticmethod
    def div(a, b):
        ##
        # Division function
        # Args:
        #     a: Division argument.
        #     b: Division argument.
        # Returns:
        #     Value of the following expression a/b.
        # Raises:
        #     ZeroDivisionError
        #
        if b == 0:
            raise ZeroDivisionError
        return a / b

    @staticmethod
    def fact(a):
        ##
        # Factorial function
        # Args:
        #     a: Factorial argument.
        # Returns:
        #     Value of following expression a!.
        # Raises:
        #     ValueError.
        if type(a) != int:
            raise ValueError("Factorial of real number.")
        elif a < 0:
            raise ValueError("Factorial of negative value.")
        elif a == 0:
            return 1
        else:
            return a * CChanMathlib.fact(a - 1)

    @staticmethod
    def pow(a, exp):
        ##
        # Power function
        # Args:
        #     a:   Base.
        #     exp: Power.
        # Returns:
        #     Value of following expression a^exp.
        # Raises:
        #     ValueError
        if type(exp) != int:
            raise ValueError("Exponent is not integer.")
        elif exp < 0:
            raise ValueError("Exponent is negative value.")
        elif exp == 0:
            return 1
        else:
            return a ** exp

    @staticmethod
    def root(a, n):
        ##
        # Root function
        # Args:
        #     a: Base.
        #     n: Order of root.
        # Returns:
        #     Value of following expression a^(1/n).
        # Raises:
        #     ValueError.
        if a < 0:
            raise ValueError("Order of root is zero or negative.")
        elif n <= 0:
            raise ValueError("Base value is negative or zero.")
        else:
            return a ** (1 / n)

    @staticmethod
    def ln(a):
        ##
        # Natural logarithm function
        # Args:
        #     a: Natural logarithm.
        # Returns:
        #     Value of following expression ln(a).
        # Raises:
        #     ValueError.
        if a <= 0:
            raise ValueError("Natural logarithm argument is zero or negative.")
        elif a == 1:
            return 0
        else:
            n = 10000000000.0
            return n * ((a ** (1/n)) - 1)

    @staticmethod
    def analyze(expr):
        ##
        # Checks syntax of expression and determines the correct order of basic operations needed
        # to evaluate the expression
        # Args:
        #     expr: expression represented as a string of supported mathematical functions and their operands
        # Returns:
        #     List of operations in correct order to evaluate the expression
        # Raises:
        #     ValueError, SyntaxError, ZeroDivisionError.
        pass

    @staticmethod
    def eval(expr):
        ##
        # Eval function
        # Args:
        #     expr: expression represented as a string of supported mathematical functions and their operands
        # Returns:
        #     Value of expr after evaluation.
        # Raises:
        #     ValueError, SyntaxError, ZeroDivisionError.
        pass
