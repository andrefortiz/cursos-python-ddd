import abc
import uuid

from utils.interfaces.IEntity import IEntity


class AbstractEntity(IEntity, abc.ABC):
    id = None  # usado para os campos chaves que são auto-incremented
    codigo = None  # usado para os campos chave que não são auto-incremented

    @abc.abstractmethod
    def __init__(self, **kwargs):
        if "id" in kwargs:
            self.id = kwargs.__getitem__("id")
        else:
            self.id = uuid.uuid1().__str__()
