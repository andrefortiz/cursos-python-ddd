import unittest

from util.AssertExtensions import AssertExtensions
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.Subsidiarias.Subsidiaria import Subsidiaria


class test_contrato(unittest.TestCase):
    @staticmethod
    def test_deve_criar_subsidiaria():
        nome = "Campo Grande"
        new_city = Subsidiaria(nome)
        assert new_city.nome == nome

    @staticmethod
    def test_deve_validar_nome():
        mensagem = "Nome da subsidiária é inválido"
        AssertExtensions.throws_with_message(lambda: Subsidiaria(None), DomainException, mensagem)
        AssertExtensions.throws_with_message(lambda: Subsidiaria(""), DomainException, mensagem)




