from __future__ import annotations

from typing import List, Type

from manutencao.solicitacao.aplicacao.AbstractUnitOfWork import AbstractUnitOfWork

from utils.exceptions.UnitOfWorkException import UnitOfWorkException
from utils.interfaces.IRepository import TRepository
from utils.interfaces.IUnitOfWork import IUnitOfWork

"""
O metodo __init__ não deve ser implementado porque o dict já serve pra passar
os parametros que no minimo devem ser: session_factory=, session_repository=
Foi feito dessa forma para que fosse possível passar mais de um repositorio se necessário
"""


class UnitOfWork(AbstractUnitOfWork, IUnitOfWork):

    """
    O repositorio principal deve ser sempre o primeiro da lista do parametro "repositories="
    """

    def __init__(self, session_factory, repositories=List[Type[TRepository]]):
        self.session_factory = session_factory
        self.repositories = repositories

        UnitOfWorkException.lancar_quando(self.session_factory is None, "Parâmetro session_factory não informado")
        UnitOfWorkException.lancar_quando(self.repositories is None or self.repositories.__len__() == 0,
                                          "Nenhuma classe de repositório foi informada")

    def __enter__(self) -> UnitOfWork:

        self.session = self.session_factory.get_session()

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

        UnitOfWorkException.lancar_quando(self.session_repository is None, "Repositório principal não foi informado")

        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
        self.session.close()








