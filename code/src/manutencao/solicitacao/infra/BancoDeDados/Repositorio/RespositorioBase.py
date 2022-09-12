import abc

from manutencao.solicitacao.dominio.AbstractEntity import AbstractEntity
from utils.interfaces.abstract_repository import AbstractRepository


class RepositorioBase(AbstractRepository, abc.ABC):

    def __init__(self, session):
        self.session = session

    @abc.abstractmethod
    def set_session(self, session):
        self.session = session

    @abc.abstractmethod
    def add(self, entity: AbstractEntity):
        self.session.add(entity)

    @abc.abstractmethod
    def get(self, reference: str):
        pass

    @abc.abstractmethod
    def list(self):
        pass
