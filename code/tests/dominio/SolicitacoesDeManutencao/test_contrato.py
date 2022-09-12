import datetime
import unittest

from util.AssertExtensions import AssertExtensions
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Contrato import Contrato


class test_contrato(unittest.TestCase):

    numero_contrato = "1"
    nome_terceirizada = "Limpezas Ltda"
    cnpj_terceirizada = "12123123000199"
    gestor = "Sr Cassia"

    @staticmethod
    def criar_contrato():
        return Contrato(
            "1",
            "Limpezas Ltda",
            "12123123000199",
            "Sr Cassia",
            datetime.datetime(2022, 10, 10)
        )

    @staticmethod
    def criar_contrato_sob_medida(**kwargs):
        return Contrato(
            AssertExtensions.return_param("numero", **kwargs),
            AssertExtensions.return_param("nome_da_terceirizada", **kwargs),
            AssertExtensions.return_param("cnpj_da_terceirizada", **kwargs),
            AssertExtensions.return_param("gestor_do_contrato", **kwargs),
            AssertExtensions.return_param("data_final_da_vigencia", **kwargs),
        )

    def test_deve_criar_solicitante(self):
        new_contrato = Contrato(
            self.numero_contrato,
            self.nome_terceirizada,
            self.cnpj_terceirizada,
            self.gestor,
            datetime.datetime(2022, 10, 10))

        new = self.criar_contrato()
        assert new.numero == new_contrato.numero
        assert new.nome_da_terceirizada == new_contrato.nome_da_terceirizada
        assert new.cnpj_da_terceirizada == new_contrato.cnpj_da_terceirizada
        assert new.gestor_do_contrato == new_contrato.gestor_do_contrato
        assert new.data_final_da_vigencia == new_contrato.data_final_da_vigencia

    def test_deve_validar_numero_contrato(self):
        mensagem = "Número do contrato é inválido"
        AssertExtensions.throws_with_message(lambda: self.criar_contrato_sob_medida(), DomainException, mensagem)

    def test_deve_validar_nome_da_terceirizada(self):
        mensagem = "Nome da terceirizada é inválido"
        AssertExtensions.throws_with_message(lambda: self.criar_contrato_sob_medida(
                                                numero="1"), DomainException, mensagem)

    def test_deve_validar_cnpj_da_terceirazada(self):
        mensagem = "CNPJ da terceirizada é inválido"
        AssertExtensions.throws_with_message(lambda: self.criar_contrato_sob_medida(
                                                numero="1",
                                                nome_da_terceirizada=self.nome_terceirizada),
                                             DomainException, mensagem)
        AssertExtensions.throws_with_message(lambda: self.criar_contrato_sob_medida(
                                                numero="1",
                                                nome_da_terceirizada=self.nome_terceirizada,
                                                cnpj_da_terceirizada="99"),
                                             DomainException, mensagem)

    def test_deve_validar_gestor_do_contrato(self):
        mensagem = "Gestor do contrato é inválido"
        AssertExtensions.throws_with_message(lambda: self.criar_contrato_sob_medida(
                                                numero="1",
                                                nome_da_terceirizada=self.nome_terceirizada,
                                                cnpj_da_terceirizada=self.cnpj_terceirizada),
                                             DomainException, mensagem)

    def test_deve_validar_data_de_fim_da_vigencia(self):
        mensagem = "Vigência do contrato esta vencido"
        data_de_fim_da_vigencia = datetime.datetime(2019, 10, 10)

        AssertExtensions.throws_with_message(lambda: self.criar_contrato_sob_medida(
                                                numero="1",
                                                nome_da_terceirizada=self.nome_terceirizada,
                                                cnpj_da_terceirizada=self.cnpj_terceirizada,
                                                gestor_do_contrato="Sr Andre",
                                                data_final_da_vigencia=data_de_fim_da_vigencia),
                                             DomainException, mensagem)



