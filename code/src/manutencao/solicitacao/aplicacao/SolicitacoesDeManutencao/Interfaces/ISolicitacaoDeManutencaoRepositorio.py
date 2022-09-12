import abc

from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from utils.interfaces.IRepository import IRepository


class ISolicitacaoDeManutencaoRepositorio(IRepository, abc.ABC):
    @staticmethod
    def name():
        return "solicitacao_de_manutencao_repositorio"

    @abc.abstractmethod
    def __init__(self, session):
        pass

    @abc.abstractmethod
    def add(self, entity: SolicitacaoDeManutencao):
        pass

    @abc.abstractmethod
    def get(self, reference: str) -> SolicitacaoDeManutencao:
        pass

    @abc.abstractmethod
    def list(self):
        pass

    @abc.abstractmethod
    def obter_pendentes_do_tipo(self,
                                tipo_de_solicitacao_de_manutecao: TipoDeSolicitacaoDeManutencao,
                                identificador_da_subsidiaria: str):
        pass

    @abc.abstractmethod
    def obter_pendentes_da(self,
                                identificador_da_subsidiaria: str):
        pass