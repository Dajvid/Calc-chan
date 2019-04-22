# @package CChanMathlib
#  Mathematical library for CalcChan calculator.
import re
import sys

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
    def tokenize(expr):
        result = []
        new = ""
        while(expr != ""):
            expr = expr.lstrip()
            if (re.match(r"\+", expr)):
                match = re.match(r"\+", expr)
                match = match.group(0)
                new = ("+", match)
            elif (re.match(r"-", expr)):
                match = re.match(r"-", expr)
                match = match.group(0)
                new = ("-", match)
            elif (re.match(r"\*", expr)):
                match = re.match(r"\*", expr)
                match = match.group(0)
                new = ("*", match)
            elif (re.match(r"/", expr)):
                match = re.match(r"/", expr)
                match = match.group(0)
                new = ("/", match)
            elif (re.match(r"\^", expr)):
                match = re.match(r"\^", expr)
                match = match.group(0)
                new = ("^", match)
            elif (re.match(r"√", expr)):
                match = re.match(r"√", expr)
                match = match.group(0)
                new = ("√", match)
            elif (re.match(r"\(", expr)):
                match = re.match(r"\(", expr)
                match = match.group(0)
                new = ("(", match)
            elif (re.match(r"\)", expr)):
                match = re.match(r"\)", expr)
                match = match.group(0)
                new = (")", match)
            elif (re.match(r"^\d*\.\d*", expr)):
                match = re.match(r"^\d*\.\d*", expr)
                match = match.group(0)
                new = ("i", float(match))
            elif (re.match(r"([0-9]+)", expr)):
                match = re.match(r"([0-9]+)", expr)
                match = match.group(0)
                new = ("i", int(match))
            elif (re.match(r"ln", expr)):
                match = re.match(r"ln", expr)
                match = match.group(0)
                new = ("ln", match)
            elif (re.match(r"\!", expr)):
                match = re.match(r"\!", expr)
                match = match.group(0)
                new = ("!", match)
            else:
                raise SyntaxError(f"Unknown character sequnce {expr} in the expression")
            result.append(new)
            expr = expr[len(match):]
        result.append(("$", "$"))

        return result

    @staticmethod
    def is_terminal(stack_item):
        e = stack_item[0]
        return (e == "+" or e == "-" or e == "*" or e == "/" or e== "^" or e== "√" or e== "(" or e== ")" or e== "i" or e== "ln" or e== "!" or e== "$")

    @staticmethod
    def get_top_terminal(stack):
        for item in reversed(stack):
            if (CChanMathlib.is_terminal(item)):
                return item
        return None

    @staticmethod
    def get_top_sequence(stack):
        for i, item in enumerate(reversed(stack)):
            if (item[0] == "<"):
                return stack[len(stack) - i:len(stack)]
        
        return None

    @staticmethod
    def is_reducible(sequnce, rules):
        stripped_sequence = []
        for item in sequnce:
            stripped_sequence.append(item[0])

        for i, rule in enumerate(rules):
            if rule == stripped_sequence:
                return i
        
        return -1

    @staticmethod
    def insert_handle(item, stack):
        for i, stack_item in enumerate(reversed(stack)):
            if (stack_item[0] == item[0]):
                stack.insert(len(stack) - i, ("<", "<"))
                return

    @staticmethod
    def minus_recovery(input, stack, in_top):
        try:
            a = input[0]
            if (in_top[0] == '-' and a[0] == 'i'):
                del(input[0])
                return (True, (a[0], a[1] * (-1)))
            return (False, a)
        except(IndexError):
            return (False, None)

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
        PSA_table = {
            "+"  : {"+" : ">", "-" : ">", "*": "<", "/": "<", "^": "<", "√": "<", "(": "<", ")": ">", "i": "<", "ln": "<", "!":  "", "$": ">"},
            "-"  : {"+" : ">", "-" : ">", "*": "<", "/": "<", "^": "<", "√": "<", "(": "<", ")": ">", "i": "<", "ln": "<", "!":  "", "$": ">"},
            "*"  : {"+" : ">", "-" : ">", "*": ">", "/": ">", "^": "<", "√": "<", "(": "<", ")": ">", "i": "<", "ln": "<", "!":  "", "$": ">"},
            "/"  : {"+" : ">", "-" : ">", "*": ">", "/": ">", "^": "<", "√": "<", "(": "<", ")": ">", "i": "<", "ln": "<", "!":  "", "$": ">"},
            "^"  : {"+" : ">", "-" : ">", "*": ">", "/": ">", "^": "<", "√": "<", "(": "<", ")": ">", "i": "<", "ln": "<", "!":  "", "$": ">"},
            "√"  : {"+" : ">", "-" : ">", "*": ">", "/": ">", "^": "<", "√": "<", "(": "<", ")": ">", "i": "<", "ln": "<", "!":  "", "$": ">"},
            "("  : {"+" : "<", "-" : "<", "*": "<", "/": "<", "^": "<", "√": "<", "(": "<", ")": "=", "i": "<", "ln": "<", "!": "<", "$":  ""},
            ")"  : {"+" : ">", "-" : ">", "*": ">", "/": ">", "^": ">", "√": ">", "(":  "", ")": ">", "i":  "", "ln":  "", "!": ">", "$": ">"},
            "i"  : {"+" : ">", "-" : ">", "*": ">", "/": ">", "^": ">", "√": ">", "(":  "", ")": ">", "i":  "", "ln":  "", "!": ">", "$": ">"},
            "ln" : {"+" :  "", "-" :  "", "*":  "", "/":  "", "^":  "", "√":  "", "(": "=", ")":  "", "i":  "", "ln":  "", "!":  "", "$":  ""},
            "!"  : {"+" : ">", "-" : ">", "*": ">", "/": ">", "^": ">", "√": ">", "(":  "", ")": ">", "i":  "", "ln":  "", "!": ">", "$": ">"},
            "$"  : {"+" : "<", "-" : "<", "*": "<", "/": "<", "^": "<", "√": "<", "(": "<", ")":  "", "i": "<", "ln": "<", "!": "<", "$":  ""},
        }

        rules = [
            ["E", "+", "E"],           #0
            ["E", "-", "E"],           #1
            ["E", "*", "E"],           #2
            ["E", "/", "E"],           #3 
            ["E", "^", "E"],           #4
            ["E", "√", "E"],           #5
            ["(", "E", ")"],           #6
            ["i"],                     #7
            ["ln", "(", "E", ")"],     #8
            ["E", "!"],                #9
            ["-", "E"],                #10
        ]

        stack = [("$", "$")]
        input = CChanMathlib.tokenize(expr)

        in_top = input[0]
        del(input[0])

        while True:
            stack_top = CChanMathlib.get_top_terminal(stack)
            operation = PSA_table[stack_top[0]][in_top[0]]
            if (stack_top[0] == "$" and in_top[0] == "$"):
                res = stack.pop()
                return(res[1])
            elif (operation == "="):
                stack.append(in_top)
                in_top = input[0]
                del(input[0])

            elif (operation == "<"):
                CChanMathlib.insert_handle(stack_top, stack)
                stack.append(in_top)
                in_top = input[0]
                del(input[0])
            elif (operation == ">"):
                sequence = CChanMathlib.get_top_sequence(stack)
                if (sequence == None):
                    raise SyntaxError("Unreducible sequence")
                index = CChanMathlib.is_reducible(sequence, rules)
                if (index == -1):
                    ret, in_top = CChanMathlib.minus_recovery(input, stack, in_top)
                    if (ret == False):
                        raise SyntaxError("Unreducible sequence")
                # recover from parsing 'error'
                if (index == -1):
                    pass

                # E + E
                elif (index == 0):
                    #pop arguments
                    b = stack.pop()[1]
                    stack.pop()
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", CChanMathlib.add(a, b)))
                # E - E
                elif (index == 1):
                    #pop arguments
                    b = stack.pop()[1]
                    stack.pop()
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", CChanMathlib.sub(a, b)))
                # E * E
                elif (index == 2):
                    #pop arguments
                    b = stack.pop()[1]
                    stack.pop()
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", CChanMathlib.mul(a, b)))
                # E / E
                elif (index == 3):
                    #pop arguments
                    b = stack.pop()[1]
                    stack.pop()
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", CChanMathlib.div(a, b)))
                # E ^ E
                elif (index == 4):
                    #pop arguments
                    b = stack.pop()[1]
                    stack.pop()
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", CChanMathlib.pow(a, b)))
                # E √ E
                elif (index == 5):
                    #pop arguments
                    b = stack.pop()[1]
                    stack.pop()
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", CChanMathlib.root(b, a)))
                # ( E )
                elif (index == 6):
                    #pop arguments
                    stack.pop()
                    a = stack.pop()[1]
                    stack.pop()
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", a))
                # i 
                elif (index == 7):
                    #pop arguments
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #push new nonterminal
                    stack.append(("E", a))
                    pass
                # ln ( E )
                elif (index == 8):
                    #pop arguments
                    stack.pop()
                    a = stack.pop()[1]
                    stack.pop()
                    stack.pop()
                    #pop rule handle
                    stack.pop()
                    #create new nonterminal
                    stack.append(("E", CChanMathlib.ln(a)))
                # E !
                elif (index == 9):
                    #pop arguments
                    stack.pop()
                    a = stack.pop()[1]
                    #pop rule handle
                    stack.pop()
                    #create new nonterminal
                    stack.append(("E", CChanMathlib.fact(a)))
                # - E
                elif (index == 10):
                    #pop arguments
                    a = stack.pop()[1]
                    stack.pop()
                    #pop rule handle
                    stack.pop()
                    #create new nonterminal
                    stack.append((("E"), a * -1))

                else:
                    raise SyntaxError("Unreducible sequence")

            else:
                raise SyntaxError("Unknown sequence of lexems")
