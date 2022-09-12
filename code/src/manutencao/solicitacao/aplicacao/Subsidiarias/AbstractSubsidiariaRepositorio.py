import abc

from utils.interfaces.abstract_repository import AbstractRepository


class AbstractSubsidiariaRepositorio(AbstractRepository, abc.ABC):
    @abc.abstractmethod
    def add(self, model: any):
        pass

    @abc.abstractmethod
    def get(self, reference) -> any:
        pass

    @abc.abstractmethod
    def set_session(self, session):
        pass



