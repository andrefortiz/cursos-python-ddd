from __future__ import annotations

import abc
from typing import List, Type

from utils.interfaces.IRepository import TRepository
from utils.interfaces.IUnitOfWork import IUnitOfWork


class AbstractUnitOfWork(IUnitOfWork):
    session = None
    session_factory = None
    session_repository = None

    @abc.abstractmethod
    def __init__(self, session_factory, repositories=List[Type[TRepository]]):
        raise NotImplementedError

    @abc.abstractmethod
    def __enter__(self) -> AbstractUnitOfWork:
        raise NotImplementedError

    @abc.abstractmethod
    def __exit__(self, *args):
        raise NotImplementedError

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    @property
    def repository(self):
        return self.session_repository
