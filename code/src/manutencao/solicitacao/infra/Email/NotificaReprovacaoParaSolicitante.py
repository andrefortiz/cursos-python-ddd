from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.INotificaReprovacaoParaSolicitante import \
    INotificaReprovacaoParaSolicitante
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao


class NotificaReprovacaoParaSolicitante(INotificaReprovacaoParaSolicitante):
    def notificar(self, solicitacao_de_manutencao: SolicitacaoDeManutencao):
        pass