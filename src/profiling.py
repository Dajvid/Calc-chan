from CChanMathlib import CChanMathlib
from CChanParser import CChanParser
import sys


def average(numarray):
    if len(numarray) == 0:
        return 0
    res = 0
    for num in numarray:
        res = CChanMathlib.add(res, float(num))
    return CChanMathlib.div(res, len(numarray))


def factor(numarray):
    if len(numarray) == 0:
        return 0
    res = 0
    avg = average(numarray)
    for num in numarray:
        res = CChanMathlib.add(res, CChanMathlib.pow(float(num), 2))
    return CChanMathlib.sub(res, CChanMathlib.mul(len(numarray), CChanMathlib.pow(avg, 2)))


def std_dev(numarray):
    print(CChanParser.eval("2√(1 / ({}-1) * {})".format(len(numarray), factor(numarray))))


numarray = sys.stdin.read().split()
for i in (0, len(numarray) - 1):
    numarray[i] = numarray[i].strip()
    try:
        numarray[i] = float(numarray[i])
    except ValueError:
        print("Input sequence is not valid, please enter a sequence of numbers separated with spaces.")
        exit(1)

std_dev(numarray)