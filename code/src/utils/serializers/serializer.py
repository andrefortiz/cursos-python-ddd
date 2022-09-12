import enum
from typing import Optional, List

from sqlalchemy import inspect


class Serializer(object):

    def __init__(self, list: Optional[List[any]] = None, action: Optional[any] = None):
        self.list = list
        self.action = action

    def to_list(self):
        if self.list is not None and self.action is not None:
            return [self.action(m) for m in self.list]
        return {}

    def get_value(self, key):
        value = getattr(self, key)
        if isinstance(value, enum.Enum):
            value = value.value
        elif isinstance(value, enum.IntEnum):
            value = str(value.value)
        elif isinstance(value, Serializer):
            value = value.serialize()
        elif isinstance(value, list):
            value = value.serialize_list()
        return value

    def serialize(self):
        """return {c: getattr(self, c) for c in inspect(self).attrs.keys()}"""
        serialized = {}
        object_inspected = inspect(self, False)
        if object_inspected is None and isinstance(self, Serializer):
            for key, value in self.__dict__.items():
                to_be_serialized = key[:1] != '_'
                if to_be_serialized:
                    value = self.get_value(key)

                if to_be_serialized and value is not None:
                    serialized[key] = value
        else:
            """PRA FORÇAR QUE AS CLASSES (DE TABELAS FILHAS) SEJAM 
               CARREGADAS PELA BASE, TIVE QUE FAZER PELO INSPECT
               DEPOIS VOU TER QUE PENSAR ALGO MAIS ELABORADO"""
            for key in object_inspected.attrs.keys():
                to_be_serialized = key[:1] != '_'
                if to_be_serialized:
                    value = self.get_value(key)

                if to_be_serialized and value is not None:
                    serialized[key] = value

        return serialized

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
