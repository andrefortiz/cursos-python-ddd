import abc
from typing import TypeVar, Type


class IRepository(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def name():
        pass

    @abc.abstractmethod
    def __init__(self, session):
        pass

    @abc.abstractmethod
    def add(self, model: any):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> any:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        pass


TRepository = TypeVar("TRepository", bound=IRepository)


class RepositoryUnitOfWork:

    def __init__(self, nome, tipo=Type[TRepository]):
        self.nome = nome
        self.tipo = tipo

