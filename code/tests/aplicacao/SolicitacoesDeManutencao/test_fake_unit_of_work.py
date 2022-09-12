import unittest
from unittest.mock import patch

from aplicacao.SolicitacoesDeManutencao.fake_unit_of_work import FakeUnitOfWork
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.ISolicitacaoDeManutencaoRepositorio import \
    ISolicitacaoDeManutencaoRepositorio
from manutencao.solicitacao.aplicacao.Subsidiarias.Interface.ISubsidiariaRepositorio import ISubsidiariaRepositorio
from utils.serializers.AnonType import AnonType


class test_deve_inicializar_unit_of_work(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_deve_inicializar_unit_of_work, self).__init__(*args, **kwargs)

    @patch.multiple(ISolicitacaoDeManutencaoRepositorio, __abstractmethods__=set())
    @patch.multiple(ISubsidiariaRepositorio, __abstractmethods__=set())
    def test_deve_instanciar_unit_of_work(self):
        uow = FakeUnitOfWork(session_factory=AnonType(session="teste"),
                             repositories=[ISolicitacaoDeManutencaoRepositorio,
                                           ISubsidiariaRepositorio])

        with uow:
            assert uow.session_factory is not None
            assert uow.repository is not None
            assert uow.subsidiaria_repositorio is not None
