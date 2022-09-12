from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.ICanceladorDeSolicitacoesDeManutencaoPendentes \
    import ICanceladorDeSolicitacoesDeManutencaoPendentes
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao


class CanceladorDeSolicitacoesDeManutencaoPendentes(ICanceladorDeSolicitacoesDeManutencaoPendentes):
    def cancelar(self, solicitacoes_de_manutecao_pendentes: [SolicitacaoDeManutencao]):
        if solicitacoes_de_manutecao_pendentes is None:
            return

        for solicitacao in solicitacoes_de_manutecao_pendentes: solicitacao.cancelar()
