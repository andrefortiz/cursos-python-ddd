from sqlalchemy.exc import NoResultFound


from manutencao.solicitacao.aplicacao.Subsidiarias.Interface.ISubsidiariaRepositorio import ISubsidiariaRepositorio
from manutencao.solicitacao.dominio.Subsidiarias.Subsidiaria import Subsidiaria
from manutencao.solicitacao.infra.BancoDeDados.Repositorio.AbstractRepository import AbstractRepository


class SubsidiariaRepositorio(AbstractRepository, ISubsidiariaRepositorio):

    def __init__(self, session):
        if session is not None:
            super().__init__(session)

    def add(self, entity: Subsidiaria):
        super().add(entity)

    def get(self, reference: str) -> Subsidiaria:
        try:
            result = self.session.query(Subsidiaria).filter_by(id=reference).one()
        except NoResultFound:
            return None
        return result

    def list(self):
        return self.session.query(Subsidiaria).all()




