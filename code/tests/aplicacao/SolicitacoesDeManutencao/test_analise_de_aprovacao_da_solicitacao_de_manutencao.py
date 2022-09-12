import unittest
from unittest.mock import patch

from aplicacao.SolicitacoesDeManutencao.test_fake_unit_of_work import FakeUnitOfWork
from dominio.SolicitacoesDeManutencao.test_solicitacao_de_manutencao import test_solicitacao_de_manutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Services.AnaliseDeAprovacaoDaSolicitacaoDeManutencao import \
    AnaliseDeAprovacaoDaSolicitacaoDeManutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.AnaliseDeAprovacaoDto import AnaliseDeAprovacaoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.INotificaContextoDeServico import \
    INotificaContextoDeServico
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.INotificaReprovacaoParaSolicitante import \
    INotificaReprovacaoParaSolicitante
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.ISolicitacaoDeManutencaoRepositorio import \
    ISolicitacaoDeManutencaoRepositorio
from manutencao.solicitacao.aplicacao.Subsidiarias.Interface.ISubsidiariaRepositorio import ISubsidiariaRepositorio
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from util.AssertExtensions import AssertExtensions
from util.AssertMethodsWereCalled import AssertMethodsWereCalled
from util.MethodIsCalled import MethodIsCalled
from utils.serializers.AnonType import AnonType


class test_analise_de_aprovacao_da_solicitacao_de_manutencao(unittest.TestCase):

    dto = AnaliseDeAprovacaoDto(
        1,
        "Ricardo José",
        "1",
        True,
    )

    @patch.multiple(ISolicitacaoDeManutencaoRepositorio, __abstractmethods__=set())
    @patch.multiple(ISubsidiariaRepositorio, __abstractmethods__=set())
    @patch.multiple(INotificaReprovacaoParaSolicitante, __abstractmethods__=set())
    @patch.multiple(INotificaContextoDeServico, __abstractmethods__=set())
    def __init__(self, *args, **kwargs):
        super(test_analise_de_aprovacao_da_solicitacao_de_manutencao, self).__init__(*args, **kwargs)

        uow = FakeUnitOfWork(session_factory=AnonType(session="teste"),
                             repositories=[ISolicitacaoDeManutencaoRepositorio,
                                           ISubsidiariaRepositorio])

        with uow:
            assert uow.session_factory is not None
            assert uow.repository is not None

        self.notifica_reprovacao_para_solicitante = INotificaReprovacaoParaSolicitante()
        self.notifica_contexto_de_servico = INotificaContextoDeServico()
        self.analisador = AnaliseDeAprovacaoDaSolicitacaoDeManutencao(
            uow,
            self.notifica_reprovacao_para_solicitante,
            self.notifica_contexto_de_servico,
        )

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    def test_deve_validar_solicitacao_de_manutencao_a_ser_analisada(self, mock_get):
        mensagem = "Solicitação não encontrada"
        mock_get.return_value = test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao()
        with AssertMethodsWereCalled(
                [MethodIsCalled(ISolicitacaoDeManutencaoRepositorio, "get")]):
            AssertExtensions.throws_with_message(lambda:
                                                 self.analisador.analisar(self.dto), DomainException, mensagem)

        mock_get.assert_called()

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    def test_deve_reprovar_soliciacao_de_manutencao(self, mock_get):
        mock_get.return_value = test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao()
        self.dto.aprovado = False
        with AssertMethodsWereCalled(
                [MethodIsCalled(ISolicitacaoDeManutencaoRepositorio, "get", True),
                 MethodIsCalled(SolicitacaoDeManutencao, "reprovar")]):
            self.analisador.analisar(self.dto)

        mock_get.assert_called()

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    def test_deve_notificar_solicitante_sobre_reprovacao(self, mock_get):
        mock_get.return_value = test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao()
        self.dto.aprovado = False
        with AssertMethodsWereCalled(
                [MethodIsCalled(ISolicitacaoDeManutencaoRepositorio, "get", True),
                 MethodIsCalled(SolicitacaoDeManutencao, "reprovar"),
                 MethodIsCalled(INotificaReprovacaoParaSolicitante, "notificar")]):
            self.analisador.analisar(self.dto)

        mock_get.assert_called()

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    def test_deve_aprovar_soliciacao_de_manutencao(self, mock_get):
        mock_get.return_value = test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao()
        self.dto.aprovado = True
        with AssertMethodsWereCalled(
                [MethodIsCalled(ISolicitacaoDeManutencaoRepositorio, "get", True),
                 MethodIsCalled(SolicitacaoDeManutencao, "aprovar")]):
            self.analisador.analisar(self.dto)

        mock_get.assert_called()

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    def test_nao_deve_notificar_solicitante_quando_aprovado(self, mock_get):
        mock_get.return_value = test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao()
        self.dto.aprovado = True
        with AssertMethodsWereCalled(
                [MethodIsCalled(ISolicitacaoDeManutencaoRepositorio, "get", True),
                 MethodIsCalled(SolicitacaoDeManutencao, "aprovar"),
                 MethodIsCalled(INotificaReprovacaoParaSolicitante, "notificar", do_not_should_be_call=True),]):
            self.analisador.analisar(self.dto)

        mock_get.assert_called()

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    def test_deve_notificar_contexto_de_servico_sobre_aprovacao(self, mock_get):
        mock_get.return_value = test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao()
        self.dto.aprovado = True
        with AssertMethodsWereCalled(
                [MethodIsCalled(ISolicitacaoDeManutencaoRepositorio, "get", True),
                 MethodIsCalled(SolicitacaoDeManutencao, "aprovar"),
                 MethodIsCalled(INotificaContextoDeServico, "notificar")]):
            self.analisador.analisar(self.dto)

        mock_get.assert_called()

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    def test_nao_deve_notificar_contexto_de_servico_quando_reprovado(self, mock_get):
        mock_get.return_value = test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao()
        self.dto.aprovado = False
        with AssertMethodsWereCalled(
                [MethodIsCalled(ISolicitacaoDeManutencaoRepositorio, "get", True),
                 MethodIsCalled(SolicitacaoDeManutencao, "reprovar"),
                 MethodIsCalled(INotificaContextoDeServico, "notificar", do_not_should_be_call=True), ]):
            self.analisador.analisar(self.dto)

        mock_get.assert_called()


























