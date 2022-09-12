import abc

from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao


class INotificaReprovacaoParaSolicitante(abc.ABC):
    @abc.abstractmethod
    def notificar(self, solicitacao_de_manutencao: SolicitacaoDeManutencao):
        pass