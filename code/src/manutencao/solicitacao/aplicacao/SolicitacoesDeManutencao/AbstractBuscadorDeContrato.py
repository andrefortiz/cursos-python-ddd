import abc

from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.ContratoDto import ContratoDto


class AbstractBuscadorDeContrato(abc.ABC):
    @abc.abstractmethod
    def buscar(self, numero: str) -> ContratoDto:
        pass