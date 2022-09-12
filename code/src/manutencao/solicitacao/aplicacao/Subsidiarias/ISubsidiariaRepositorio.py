import abc

from utils.interfaces.IRepository import IRepository


class ISubsidiariaRepositorio(IRepository, abc.ABC):
    @staticmethod
    def name():
        return "subsidiaria_repositorio"

    @abc.abstractmethod
    def __init__(self, session):
        pass

    @abc.abstractmethod
    def add(self, model: any):
        pass

    @abc.abstractmethod
    def get(self, reference) -> any:
        pass

    @abc.abstractmethod
    def list(self):
        pass
