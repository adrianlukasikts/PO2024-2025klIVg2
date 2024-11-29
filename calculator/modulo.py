from divide_by_zero import DivideByZero
from two_operation import TwoOperation


class Modulo(TwoOperation):
    def calculate(self):
        if self.value2 == 0:
            raise DivideByZero()
        return self.value1 % self.value2

