import unittest

from util.AssertExtensions import AssertExtensions
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Autor import Autor


class test_contrato(unittest.TestCase):

    @staticmethod
    def test_deve_criar_solicitante():
        identificador = 1
        nome = "Andre"
        new = Autor(1, "Andre")
        assert new.identificador == identificador
        assert new.nome == nome

    @staticmethod
    def test_deve_validar_nome():
        mensagem = "Nome é inválido"
        AssertExtensions.throws_with_message(lambda: Autor(1, None), DomainException, mensagem)
        AssertExtensions.throws_with_message(lambda: Autor(1, ""), DomainException, mensagem)




