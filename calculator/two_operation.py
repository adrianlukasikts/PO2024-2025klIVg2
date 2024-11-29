from abc import ABC

from one_operation import OneOperation


class TwoOperation(OneOperation, ABC):
    def __init__(self, value1: float, value2: float):
        super().__init__(value1)
        self.value2 = value2

