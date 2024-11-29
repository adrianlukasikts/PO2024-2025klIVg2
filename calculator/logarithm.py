import math

from two_operation import TwoOperation


class IncorrectArguments(Exception):
    pass


class Logarithm(TwoOperation):
    def calculate(self):
        if self.value1 == 1 or self.value1 <= 0 or self.value2 <= 0:
            raise IncorrectArguments()
        return math.log(self.value2, self.value1)
