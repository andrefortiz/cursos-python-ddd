from typing import List, Type


from utils.exceptions.UnitOfWorkException import UnitOfWorkException
from utils.interfaces.IRepository import TRepository, RepositoryUnitOfWork
from utils.interfaces.IUnitOfWork import IUnitOfWork

"""
O metodo __init__ não deve ser implementado porque o dict já serve pra passar
os parametros que no minimo devem ser: session_factory=, session_repository=
Foi feito dessa forma para que fosse possível passar mais de um repositorio se necessário
"""


class FakeUnitOfWork(IUnitOfWork):
    #session = None

    """
    O repositorio principal deve ser sempre o primeiro da lista do parametro "repositories="
    """
    def __init__(self, session_factory, repositories=List[RepositoryUnitOfWork]):
        self.session_factory = session_factory
        self.repositories = repositories

        UnitOfWorkException.lancar_quando(self.repositories is None or self.repositories.__len__() == 0,
                                          "Nenhuma classe de repositório foi informada")

    def __enter__(self):
        UnitOfWorkException.lancar_quando(self.session_factory is None, "Parâmetro session_factory não informado")

        self.session = self.session_factory

        for index, repository in enumerate(self.repositories):
            UnitOfWorkException.lancar_quando(not hasattr(repository, "name"),
                                              "Repositorio informado não possui o metodo ""name""")

            instance = None
            if hasattr(self, repository.name()):
                instance = getattr(self, repository.name())

            if instance is None:
                instance = repository(self.session)
                setattr(self, repository.name(), instance)
                if index == 0:
                    self.session_repository = instance

        UnitOfWorkException.lancar_quando(self.session_repository is None, "Repositorio principal não foi informado")

        return self

    def __exit__(self, *args):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    @property
    def repository(self):
        return self.session_repository

    def get_session(self):
        return self.session

