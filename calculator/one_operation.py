from abc import abstractmethod, ABC

class OneOperation(ABC):
    def __init__(self, value1: float):
        self.value1 = value1

    @abstractmethod
    def calculate(self):
        pass