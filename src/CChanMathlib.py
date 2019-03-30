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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
        pass

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
