## @package CChanMathlib
#  Mathematical library for CalcChan calculator.

class CChanMathlib:
    def fact(self, a):
        ##
        # Factorial function
        # Args:
        #     a: Factorial argument.
        # Returns:
        #     Value of following expression a!.
        # Raises:
        #     ValueError.
        pass

    def pow(self, a, exp):
        ##
        # Power function
        # Args:
        #     a:   Base.
        #     exp: Power.
        # Returns:
        #     Value of following expression a^exp.
        # Raises:
        #
        pass

    def root(self, a, n):
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

    def tan(self, a):
        ##
        # Tangents function
        # Args:
        #     a: Tangents argument.
        # Returns:
        #     Value of following expression tan(a).
        # Raises:
        #     ValueError.
        pass

    def analyze(self, expr):
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

    def eval(self, expr):
        ##
        # Eval function
        # Args:
        #     expr: expression represented as a string of supported mathematical functions and their operands
        # Returns:
        #     Value of expr after evaluation.
        # Raises:
        #     ValueError, SyntaxError, ZeroDivisionError.
        pass
