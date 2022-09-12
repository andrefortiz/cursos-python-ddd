from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.INotificaContextoDeServico import \
    INotificaContextoDeServico
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao


class NotificaContextoDeServico(INotificaContextoDeServico):
    def notificar(self, solicitacao_de_manutencao: SolicitacaoDeManutencao):
        pass