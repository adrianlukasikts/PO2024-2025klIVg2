from two_operation import TwoOperation


class Power(TwoOperation):
    def calculate(self):
        return self.value1 ** self.value2
