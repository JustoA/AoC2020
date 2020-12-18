import copy
import re

import inp  # my [REDACTED] input parser


# I can trick python into ignoring order of operations while parsing by making subtract do multiplication instead.. I think.
class MyInt(int):
    def __add__(self, other):
        return MyInt(int(self) + int(other))  # need to make regular int again otherwise we _infinite loop_

    def __sub__(self, other):
        return MyInt(int(self) * int(other))

    def __mul__(self, other):
        return MyInt(int(self) + int(other))


def evaluate_eq(eq):
    eq = re.sub('(\d)', r'MyInt(\1)', eq)
    eq = eq.replace('*', '-')
    return eval(eq)


def main():
    instream = inp.parse_file_str()
    ans = 0
    for eq in instream:
        ans += evaluate_eq(eq)
    return ans


def evaluate_eq2(eq):
    eq = re.sub('(\d)', r'MyInt(\1)', eq)
    eq = eq.replace('*', "-").replace('+', '*')
    return eval(eq)


def main2():
    instream = inp.parse_file_str()
    ans = 0
    for eq in instream:
        ans += evaluate_eq2(eq)
    return ans


print(f'Part 1: {main()}')
print(f'Part 2: {main2()}')
