from one_operation import OneOperation


class NegativeNumber(Exception):
    pass


class Factorial(OneOperation):
    def calculate(self):
        value1 = int(self.value1)
        if value1 < 0:
            raise NegativeNumber()
        result = 1
        for i in range(2, value1 + 1):
            result *= i
        return result
