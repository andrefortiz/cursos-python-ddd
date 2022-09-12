import pytest

from manutencao.solicitacao.dominio.DomainException import DomainException


class AssertExtensions:

    @staticmethod
    def throws_with_message(action, expected_exception, message_expected):
        with pytest.raises(expected_exception) as e:
            try:
                action()
            except Exception as err:
                raise err
        assert e.value.args[0] == message_expected

    @staticmethod
    def return_param(nome_param, **kwargs):
        if len(kwargs) > 0:
            if nome_param in kwargs:
                return kwargs[nome_param]
        return None
