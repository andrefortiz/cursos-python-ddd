from typing import List

from sqlalchemy.exc import NoResultFound

from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.ISolicitacaoDeManutencaoRepositorio import \
    ISolicitacaoDeManutencaoRepositorio
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.StatusDaSolicitacao import StatusDaSolicitacao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from manutencao.solicitacao.infra.BancoDeDados.Repositorio.AbstractRepository import AbstractRepository


class SolicitacaoDeManutencaoRepositorio(AbstractRepository, ISolicitacaoDeManutencaoRepositorio):

    def __init__(self, session):
        if session is not None:
            super().__init__(session)

    def add(self, entity: SolicitacaoDeManutencao):
        super().add(entity)

    def get(self, reference: str) -> SolicitacaoDeManutencao:
        try:
            return self.session.query(SolicitacaoDeManutencao).filter_by(id=reference).one()
        except NoResultFound:
            return None

    def list(self):
        return self.session.query(SolicitacaoDeManutencao).all()

    def obter_pendentes_do_tipo(self,
                                tipo_de_solicitacao_de_manutecao: TipoDeSolicitacaoDeManutencao,
                                identificador_da_subsidiaria: str):

        return self.session.query(SolicitacaoDeManutencao).filter_by(
            tipo_de_solicitacao_de_manutencao=tipo_de_solicitacao_de_manutecao,
            identificador_da_subsidiaria=identificador_da_subsidiaria,
            status_da_solicitacao=StatusDaSolicitacao.Pendente
            ).all()

    def obter_pendentes_da(self, identificador_da_subsidiaria: str) \
            -> List[SolicitacaoDeManutencao]:

        result = self.session.query(SolicitacaoDeManutencao).filter_by(
            identificador_da_subsidiaria=identificador_da_subsidiaria,
            status_da_solicitacao=StatusDaSolicitacao.Pendente
        )

        return result.all()


