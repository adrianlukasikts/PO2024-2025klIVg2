from one_operation import OneOperation
from math import sin


class Sinus(OneOperation):

    def calculate(self):
        return sin(self.value1)
