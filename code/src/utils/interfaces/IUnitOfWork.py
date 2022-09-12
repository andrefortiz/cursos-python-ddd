from __future__ import annotations
import abc


class IUnitOfWork(abc.ABC):

    @abc.abstractmethod
    def __enter__(self) -> IUnitOfWork:
        pass

    @abc.abstractmethod
    def __exit__(self, *args):
        pass

    @abc.abstractmethod
    def commit(self):
        pass

    @abc.abstractmethod
    def rollback(self):
        pass

    @property
    @abc.abstractmethod
    def repository(self):
        pass
