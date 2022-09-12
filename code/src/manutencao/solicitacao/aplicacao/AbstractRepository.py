import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, entity: any):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> any:
        raise NotImplementedError



