import abc


class IUnitOfWork(abc.ABC):

    @abc.abstractmethod
    def __init__(self, session_factory):
        pass

    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, *args):
        pass

    @abc.abstractmethod
    def get_session(self):
        pass

    @abc.abstractmethod
    def commit(self):
        pass

    @abc.abstractmethod
    def rollback(self):
        pass





