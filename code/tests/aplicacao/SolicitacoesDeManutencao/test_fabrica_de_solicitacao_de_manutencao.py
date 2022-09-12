import datetime
import unittest
from unittest.mock import patch

from aplicacao.SolicitacoesDeManutencao.test_fake_unit_of_work import FakeUnitOfWork
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.IBuscadorDeContrato import \
    IBuscadorDeContrato
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.ISolicitacaoDeManutencaoRepositorio import \
    ISolicitacaoDeManutencaoRepositorio
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.ContratoDto import ContratoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Fabricas.FabricaDeSolicitacaoDeManutencao import \
    FabricaDeSolicitacaoDeManutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.SolicitacaoDeManutencaoDto import \
    SolicitacaoDeManutencaoDto
from manutencao.solicitacao.aplicacao.Subsidiarias.Interface.ISubsidiariaRepositorio import ISubsidiariaRepositorio
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from manutencao.solicitacao.dominio.Subsidiarias.Subsidiaria import Subsidiaria
from util.AssertExtensions import AssertExtensions
from utils.serializers.AnonType import AnonType


class test_fabrica_de_solicitacao_de_manutencao(unittest.TestCase):

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

    @patch.multiple(ISolicitacaoDeManutencaoRepositorio, __abstractmethods__=set())
    @patch.multiple(ISubsidiariaRepositorio, __abstractmethods__=set())
    @patch.multiple(IBuscadorDeContrato, __abstractmethods__=set())
    def __init__(self, *args, **kwargs):
        super(test_fabrica_de_solicitacao_de_manutencao, self).__init__(*args, **kwargs)

        uow = FakeUnitOfWork(session_factory=AnonType(session="teste"),
                             repositories=[ISolicitacaoDeManutencaoRepositorio,
                                           ISubsidiariaRepositorio]
                             )

        with uow:
            assert uow.session_factory is not None
            assert uow.repository is not None
            assert uow.subsidiaria_repositorio is not None

        self.buscador_de_contrato = IBuscadorDeContrato()
        self.fabricador = FabricaDeSolicitacaoDeManutencao(
            uow,
            self.buscador_de_contrato)

    @patch.multiple(ISubsidiariaRepositorio, __abstractmethods__=set())
    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'get')
    @patch.object(IBuscadorDeContrato, 'buscar')
    def test_deve_validar_subsidiaria(self, mock_buscar, mock_get):
        mock_get.return_value = Subsidiaria("ANDRE", id="")
        mock_buscar.return_value = self.contrato_dto
        mensagem = "Subsidiária é inválida"

        AssertExtensions.throws_with_message(lambda: self.fabricador.fabricar(self.dto),
                                             DomainException, mensagem)

    @patch.multiple(ISubsidiariaRepositorio, __abstractmethods__=set())
    @patch.object(ISubsidiariaRepositorio, 'get')
    @patch.object(IBuscadorDeContrato, 'buscar')
    def test_deve_salvar_solicitacao_de_manutecao(self, mock_buscar, mock_get):
        mock_get.return_value = Subsidiaria("ANDRE", id="XPTO-ABC")
        mock_buscar.return_value = self.contrato_dto

        self.fabricador.fabricar(self.dto)

    @patch.multiple(ISubsidiariaRepositorio, __abstractmethods__=set())
    @patch.object(ISubsidiariaRepositorio, 'get')
    @patch.object(IBuscadorDeContrato, 'buscar')
    def test_deve_validar_contrato(self, mock_buscar, mock_get):
        mock_get.return_value = Subsidiaria("ANDRE", id="XPTO-ABC")
        mock_buscar.return_value = None

        mensagem = "Contrato não encontrado no ERP"
        AssertExtensions.throws_with_message(lambda: self.fabricador.fabricar(self.dto),
                                             DomainException, mensagem)
























