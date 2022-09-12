from sqlalchemy.orm import sessionmaker

from config import get_sqlite_engine, get_mysql_engine
from manutencao.solicitacao.infra.BancoDeDados import metadata


class BootStrap:
    def __init__(self, start_orm: bool = True):
        self.start_orm = start_orm
        if self.start_orm:
            metadata.start_tables_map()

    def get_session(self):
        if self.start_orm:
            session = sessionmaker(bind=get_mysql_engine())
            return session()
        return None



