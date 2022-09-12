import datetime
import unittest

from dominio.SolicitacoesDeManutencao.test_contrato import test_contrato
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Autor import Autor
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.StatusDaSolicitacao import StatusDaSolicitacao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from util.AssertExtensions import AssertExtensions
from utils.types.DateTime import DateTime


class test_solicitacao_de_manutencao(unittest.TestCase):

    identificador_solicitante = 1
    identificador_da_subsidiaria = "XPTO=33"
    nome_do_solicitante = "Andre Ortiz"
    tipo_de_solicitacao_de_manutencao = TipoDeSolicitacaoDeManutencao.Jardinagem
    justificativa = "Grama muito alta"
    inicio_desejado_para_manutencao = datetime.datetime(2021, 5, 5)

    @staticmethod
    def criar_solicitacao_de_manutencao():
        contrato = test_contrato.criar_contrato()
        return SolicitacaoDeManutencao(
            "XPTO=33",
            1,
            "Andre Ortiz",
            TipoDeSolicitacaoDeManutencao.Jardinagem,
            "Grama muito alta",
            contrato.numero,
            contrato.nome_da_terceirizada,
            contrato.cnpj_da_terceirizada,
            contrato.gestor_do_contrato,
            contrato.data_final_da_vigencia,
            DateTime.add_days(10),
        )

    @staticmethod
    def criar_solicitacao_de_manutencao_sob_medida(**kwargs):
        return SolicitacaoDeManutencao(
            AssertExtensions.return_param("identificador_da_subsidiaria", **kwargs),
            AssertExtensions.return_param("identificador_do_solicitante", **kwargs),
            AssertExtensions.return_param("nome_do_solicitante", **kwargs),
            AssertExtensions.return_param("tipo_de_solicitacao_de_manutencao", **kwargs),
            AssertExtensions.return_param("justificativa", **kwargs),
            AssertExtensions.return_param("numero_do_contrato", **kwargs),
            AssertExtensions.return_param("nome_da_terceirizada", **kwargs),
            AssertExtensions.return_param("cnpj_da_terceirizada", **kwargs),
            AssertExtensions.return_param("gestor_do_contrato", **kwargs),
            AssertExtensions.return_param("data_final_da_vigencia", **kwargs),
            AssertExtensions.return_param("inicio_desejado_para_manutencao", **kwargs),
        )

    def test_deve_criar_solicitacao_de_manutencao(self):
        contrato = test_contrato.criar_contrato()

        new_solicitacao = SolicitacaoDeManutencao(
            self.identificador_da_subsidiaria,
            self.identificador_solicitante,
            self.nome_do_solicitante,
            self.tipo_de_solicitacao_de_manutencao,
            self.justificativa,
            contrato.numero,
            contrato.nome_da_terceirizada,
            contrato.cnpj_da_terceirizada,
            contrato.gestor_do_contrato,
            contrato.data_final_da_vigencia,
            DateTime.add_days(10)
        )

        new = self.criar_solicitacao_de_manutencao()
        assert new.solicitante.identificador == new_solicitacao.solicitante.identificador
        assert new.solicitante.nome == new_solicitacao.solicitante.nome
        assert new.tipo_de_solicitacao_de_manutencao == new_solicitacao.tipo_de_solicitacao_de_manutencao
        assert new.justificativa == new_solicitacao.justificativa
        assert new.inicio_desejado_para_manutencao == new_solicitacao.inicio_desejado_para_manutencao

    def test_deve_validar_subsidiaria(self):
        mensagem = "Subsidiária é inválida"
        AssertExtensions.throws_with_message(lambda: self.criar_solicitacao_de_manutencao_sob_medida(),
                                             DomainException, mensagem)

    def test_deve_validar_justificativa(self):
        mensagem = "Justificativa inválida"
        AssertExtensions.throws_with_message(lambda: self.criar_solicitacao_de_manutencao_sob_medida(
                                            identificador_da_subsidiaria=self.identificador_da_subsidiaria),
                                             DomainException, mensagem)

    def test_deve_ter_data_solicitacao_de_hoje(self):
        data_solicitacao_esperada = datetime.datetime.now()

        new = self.criar_solicitacao_de_manutencao()

        assert new.data_da_solicitacao == data_solicitacao_esperada

    def test_deve_iniciar_com_status_pendente(self):
        status_da_solicitacao = StatusDaSolicitacao.Pendente

        new = self.criar_solicitacao_de_manutencao()

        assert new.status_da_solicitacao == status_da_solicitacao

    def test_deve_iniciar_com_status_pendente(self):
        status_da_solicitacao = StatusDaSolicitacao.Pendente

        new = self.criar_solicitacao_de_manutencao()

        assert new.status_da_solicitacao == status_da_solicitacao

    def test_deve_cancelar_solicitacao_de_manutecao(self):
        status_da_solicitacao = StatusDaSolicitacao.Cancelada

        new = self.criar_solicitacao_de_manutencao()
        new.cancelar()

        assert new.status_da_solicitacao == status_da_solicitacao

    def test_deve_validar_data_inicio_desejado(self):
        mensagem = "Data inicio desejado para manutenção deve ser maior que data atual"

        contrato = test_contrato.criar_contrato()

        AssertExtensions.throws_with_message(lambda: SolicitacaoDeManutencao(
                                                self.identificador_da_subsidiaria,
                                                self.identificador_solicitante,
                                                self.nome_do_solicitante,
                                                self.tipo_de_solicitacao_de_manutencao,
                                                self.justificativa,
                                                contrato.numero,
                                                contrato.nome_da_terceirizada,
                                                contrato.cnpj_da_terceirizada,
                                                contrato.gestor_do_contrato,
                                                contrato.data_final_da_vigencia,
                                                DateTime.add_days(-1)),
                                             DomainException, mensagem)

    def test_deve_reprovar_solicitacao_de_manutencao(self):
        status_da_solicitacao = StatusDaSolicitacao.Reprovada

        aprovador = Autor(1, "Reprovador")
        new = self.criar_solicitacao_de_manutencao()

        new.reprovar(aprovador)

        assert new.status_da_solicitacao == status_da_solicitacao

    def test_deve_informar_o_aprovador_da_reprovacao(self):

        aprovador = Autor(1, "Reprovador")
        new = self.criar_solicitacao_de_manutencao()

        new.reprovar(aprovador)

        assert new.aprovador == aprovador

    def test_deve_aprovar_solicitacao_de_manutencao(self):
        status_da_solicitacao = StatusDaSolicitacao.Aprovada

        aprovador = Autor(1, "Aprovador")
        new = self.criar_solicitacao_de_manutencao()

        new.aprovar(aprovador)

        assert new.status_da_solicitacao == status_da_solicitacao

    def test_deve_informar_o_aprovador_da_aprovacao(self):

        aprovador = Autor(1, "Aprovador")
        new = self.criar_solicitacao_de_manutencao()

        new.reprovar(aprovador)

        assert new.aprovador == aprovador





