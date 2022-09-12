import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, model: any):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> any:
        raise NotImplementedError

    @abc.abstractmethod
    def set_session(self, session):
        raise NotImplementedError
