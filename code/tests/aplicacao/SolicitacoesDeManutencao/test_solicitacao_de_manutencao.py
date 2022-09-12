import datetime
import unittest
from unittest.mock import patch

from aplicacao.SolicitacoesDeManutencao.test_fake_unit_of_work import FakeUnitOfWork
from dominio.SolicitacoesDeManutencao.test_solicitacao_de_manutencao import test_solicitacao_de_manutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.ContratoDto import ContratoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Fabricas.FabricaDeSolicitacaoDeManutencao import \
    FabricaDeSolicitacaoDeManutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.IBuscadorDeContrato import \
    IBuscadorDeContrato
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.ISolicitacaoDeManutencaoRepositorio import \
    ISolicitacaoDeManutencaoRepositorio
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.SolicitacaoDeManutencaoDto import \
    SolicitacaoDeManutencaoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Services.SolicitadorDeManutencao import SolicitadorDeManutencao
from manutencao.solicitacao.aplicacao.Subsidiarias.Interface.ISubsidiariaRepositorio import ISubsidiariaRepositorio
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.CanceladorDeSolicitacoesDeManutencaoPendentes import \
    CanceladorDeSolicitacoesDeManutencaoPendentes
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.ICanceladorDeSolicitacoesDeManutencaoPendentes import \
    ICanceladorDeSolicitacoesDeManutencaoPendentes
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from manutencao.solicitacao.dominio.Subsidiarias.Subsidiaria import Subsidiaria
from util.AssertMethodWasCalled import AssertMethodWasCalled
from util.AssertMethodsWereCalled import AssertMethodsWereCalled
from util.MethodIsCalled import MethodIsCalled
from utils.serializers.AnonType import AnonType


class test_solicitacao_de_manutencao(unittest.TestCase):

    dto = SolicitacaoDeManutencaoDto(
        "XPTO-ABC",
        1,
        "Ricardo José",
        TipoDeSolicitacaoDeManutencao.Jardinagem.__hash__(),
        "Grama Alta",
        "2135",
        datetime.datetime(2021, 6, 26)
    )

    contrato_dto = ContratoDto(
        dto.numero_do_contrato,
        "Grama SA",
        "99999999999999",
        "Edivaldo Pereira",
        datetime.datetime(2022, 4, 26)
    )

    solicitacoes_pendente = [
        test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao(),
        test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao(),
    ]

    #uow = None

    @patch.multiple(ICanceladorDeSolicitacoesDeManutencaoPendentes, __abstractmethods__=set())
    @patch.multiple(IBuscadorDeContrato, __abstractmethods__=set())
    @patch.multiple(ISolicitacaoDeManutencaoRepositorio, __abstractmethods__=set())
    @patch.multiple(ISubsidiariaRepositorio, __abstractmethods__=set())
    def __init__(self, *args, **kwargs):
        super(test_solicitacao_de_manutencao, self).__init__(*args, **kwargs)

        uow = FakeUnitOfWork(session_factory=AnonType(session="teste"),
                             repositories=[ISolicitacaoDeManutencaoRepositorio,
                                           ISubsidiariaRepositorio]
                             )

        with uow:
            assert uow.session_factory is not None
            assert uow.repository is not None
            assert uow.subsidiaria_repositorio is not None

        buscador_de_contrato = IBuscadorDeContrato()
        self.fabrica_de_solicitacao_de_manutencao = FabricaDeSolicitacaoDeManutencao(
            uow,
            buscador_de_contrato
        )

        self.cancelador_de_solicitacoes_de_manutencao_pendentes = ICanceladorDeSolicitacoesDeManutencaoPendentes()
        self.solicitador = SolicitadorDeManutencao(
            uow,
            self.fabrica_de_solicitacao_de_manutencao,
            self.cancelador_de_solicitacoes_de_manutencao_pendentes)

    @patch.object(ISubsidiariaRepositorio, 'get')
    @patch.object(IBuscadorDeContrato, 'buscar')
    def test_deve_salvar_solicitacao_de_manutecao(self, mock_buscar, mock_get):
        mock_get.return_value = Subsidiaria("ANDRE", id="XPTO-ABC")
        mock_buscar.return_value = self.contrato_dto

        self.solicitador.solicitar(self.dto)

    @patch.object(ICanceladorDeSolicitacoesDeManutencaoPendentes, 'cancelar',
                  CanceladorDeSolicitacoesDeManutencaoPendentes.cancelar)
    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'obter_pendentes_do_tipo')
    @patch.object(ISubsidiariaRepositorio, 'get')
    @patch.object(IBuscadorDeContrato, 'buscar')
    def test_deve_cancelar_solicitacoes_de_manutencao_pendentes_para_o_tipo_solicitacao(
            self, mock_buscar, mock_get, mock_obter_pendentes_do_tipo):
        mock_get.return_value = Subsidiaria("ANDRE", id="XPTO-ABC")
        mock_buscar.return_value = self.contrato_dto

        mock_obter_pendentes_do_tipo.return_value = self.solicitacoes_pendente

        with AssertMethodsWereCalled(
                [MethodIsCalled(ICanceladorDeSolicitacoesDeManutencaoPendentes, "cancelar"),
                 MethodIsCalled(IBuscadorDeContrato, "buscar", True)]):
            self.solicitador.solicitar(self.dto)

        with AssertMethodWasCalled(ICanceladorDeSolicitacoesDeManutencaoPendentes, "cancelar"):
            self.solicitador.solicitar(self.dto)

        mock_get.assert_called()
        mock_buscar.assert_called()
        mock_obter_pendentes_do_tipo.assert_called()





















