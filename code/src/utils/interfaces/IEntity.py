import abc


class IEntity(abc.ABC):

    @abc.abstractmethod
    def __init__(self, **kwargs):
        pass