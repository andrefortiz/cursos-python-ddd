import abc

from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from utils.interfaces.abstract_repository import AbstractRepository


class AbstractSolicitacaoDeManutencaoRepositorio(AbstractRepository, abc.ABC):
    @abc.abstractmethod
    def add(self, entity: SolicitacaoDeManutencao):
        pass

    @abc.abstractmethod
    def get(self, reference: str) -> SolicitacaoDeManutencao:
        pass

    @abc.abstractmethod
    def set_session(self, session):
        pass

    @abc.abstractmethod
    def obter_pendentes_do_tipo(self,
                                tipo_de_solicitacao_de_manutecao: TipoDeSolicitacaoDeManutencao,
                                identificador_da_subsidiaria: str):
        pass