from one_operation import OneOperation


class Absolute(OneOperation):

    def calculate(self):
        return abs(self.value1)
