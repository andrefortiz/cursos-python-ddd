import abc

from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.ContratoDto import ContratoDto


class IBuscadorDeContrato(abc.ABC):
    @abc.abstractmethod
    def buscar(self, numero: str) -> ContratoDto:
        pass