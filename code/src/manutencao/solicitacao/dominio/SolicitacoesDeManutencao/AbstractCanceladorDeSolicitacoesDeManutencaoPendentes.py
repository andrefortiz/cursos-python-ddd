import abc

from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao


class AbstractCanceladorDeSolicitacoesDeManutencaoPendentes(abc.ABC):
    @abc.abstractmethod
    def cancelar(self, solicitacoes_de_manutecao_pendentes: [SolicitacaoDeManutencao]):
        pass