import abc

from utils.interfaces.IContract import IContract


class AbstractContract(IContract, abc.ABC):

    errors = []

    def __init__(self,  dto_class):
        self.dto_class = dto_class

    def is_valid(self):
        return len(self.errors) == 0

    @abc.abstractmethod
    def validate(self):
        pass








