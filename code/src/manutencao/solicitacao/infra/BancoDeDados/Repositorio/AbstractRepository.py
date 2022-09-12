import abc

from sqlalchemy.exc import NoResultFound

from utils.interfaces.IEntity import IEntity
from utils.interfaces.IRepository import IRepository


class AbstractRepository(IRepository, abc.ABC):
    session = None

    @abc.abstractmethod
    def __init__(self, session):
        self.session = session

    @abc.abstractmethod
    def add(self, entity: IEntity):
        self.session.add(entity)

    @abc.abstractmethod
    def get(self, reference: str):
        pass

    @abc.abstractmethod
    def list(self):
        pass





