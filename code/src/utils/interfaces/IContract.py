import abc


class IContract(abc.ABC):

    @abc.abstractmethod
    def __init__(self,  domain_class):
        pass

    @abc.abstractmethod
    def is_valid(self):
        pass

    @abc.abstractmethod
    def validate(self):
        pass






