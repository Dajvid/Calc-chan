import re
from CChanMathlib import CChanMathlib
##
# @brief Class representing the Calc-chan parser library.
#
class CChanParser:
    ##
    # @brief Turns input string into list of tokens.
    #
    # @param expr Expression in a string format.
    #
    # @return List of tokens.
    #
    # @exception If input sequence expr is not recognizable, the function raises SyntaxError.
    #
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

    ##
    # @brief Determines if token is terminal.
    #
    # @param stack_item Item from stack in form of 2-tuple.
    #
    # @return True if stack_item is terminal False if it's not terminal.
    #
    @staticmethod
    def is_terminal(stack_item):
        e = stack_item[0]
        return (e == "+" or e == "-" or e == "*" or e == "/" or e== "^" or e== "√" or e== "(" or e== ")" or e== "i" or e== "ln" or e== "!" or e== "$")

    ##
    # @brief Retrieves top terminal from stack.
    #
    # @param stack PSA stack.
    #
    # @return Top terminal on stack.
    #
    @staticmethod
    def get_top_terminal(stack):
        for item in reversed(stack):
            if (CChanParser.is_terminal(item)):
                return item
        return None

    ##
    # @brief Retrieves top sequence starting with stack element ('<', '<').
    #
    # @param stack PSA stack.
    #
    # @return Top sequence from stack.
    #
    @staticmethod
    def get_top_sequence(stack):
        for i, item in enumerate(reversed(stack)):
            if (item[0] == "<"):
                return stack[len(stack) - i:len(stack)]

        return None

    ##
    # @brief Determines if given sequence is in a list of rules and can be reduced.
    #
    # @param sequence List of stack items.
    # @param rules List of rules.
    #
    # @return Index of matching rule or -1 if sequence is not reducible.
    #
    @staticmethod
    def is_reducible(sequence, rules):
        stripped_sequence = []
        for item in sequence:
            stripped_sequence.append(item[0])

        for i, rule in enumerate(rules):
            if rule == stripped_sequence:
                return i

        return -1

    ##
    # @brief Inserts sequence handle ('<', '<') after first occurrence of given stack element.
    #
    # @param item Stack element to search.
    # @param stack PSA stack.
    #
    @staticmethod
    def insert_handle(item, stack):
        for i, stack_item in enumerate(reversed(stack)):
            if (stack_item[0] == item[0]):
                stack.insert(len(stack) - i, ("<", "<"))
                return

    ##
    # @brief Attempts to recover from parsing error, if error is caused by missing operand for - operator, use - as a part of following value.
    #
    # @param input List of input tokens.
    # @param stack PSA stack.
    # @param in_top Last token taken from input.
    #
    # @return 2-tuple of True/False and new in_top element, True if error can be recovered, False otherwise.
    #
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

    ##
    # @brief Evaluates given expression.
    #
    # @param expr Expression represented as a string of supported mathematical functions and their operands.
    #
    # @return Value of expr after evaluation.
    #
    # @exception SyntaxError If the input sequence expr cannot be reduced, the function raises SyntaxError.
    # If the input sequence contains unknown symbols, the function also raises SyntaxError.
    #
    @staticmethod
    def eval(expr):
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
        input = CChanParser.tokenize(expr)

        in_top = input[0]
        del(input[0])

        while True:
            stack_top = CChanParser.get_top_terminal(stack)
            operation = PSA_table[stack_top[0]][in_top[0]]
            if (stack_top[0] == "$" and in_top[0] == "$"):
                res = stack.pop()
                return(res[1])
            elif (operation == "="):
                stack.append(in_top)
                in_top = input[0]
                del(input[0])

            elif (operation == "<"):
                CChanParser.insert_handle(stack_top, stack)
                stack.append(in_top)
                in_top = input[0]
                del(input[0])
            elif (operation == ">"):
                sequence = CChanParser.get_top_sequence(stack)
                if (sequence == None):
                    raise SyntaxError("Unreducible sequence")
                index = CChanParser.is_reducible(sequence, rules)
                if (index == -1):
                    ret, in_top = CChanParser.minus_recovery(input, stack, in_top)
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
                raise SyntaxError("Unknown sequence of tokens")