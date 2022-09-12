import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

import config
#  PARA SER USADO O ORM COM MAPPER
from manutencao.solicitacao.infra.BancoDeDados.metadata import metadata, start_tables_map


@pytest.fixture(scope='session')
def mysql_db():
    engine = create_engine(config.get_mysql_uri(), isolation_level='SERIALIZABLE')
    config.wait_for_mysql_to_come_up(engine)
    metadata.create_all(engine)

    return engine

@pytest.fixture
def session_factory_mysql_db_mapper(mysql_db):
    start_tables_map()
    yield sessionmaker(bind=mysql_db)
    clear_mappers()

@pytest.fixture
def in_memory_db_mapper():
    engine = create_engine('sqlite:///:memory:', echo=True)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def in_real_db_mapper():
    engine = create_engine('sqlite:///' + os.path.join(config.BASE_DIR, 'db_mapper.sqlite3'), echo=True)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session_factory_memory_db_mapper(in_memory_db_mapper):
    start_tables_map()
    yield sessionmaker(bind=in_memory_db_mapper)
    clear_mappers()


@pytest.fixture
def session_factory_real_db_mapper(in_real_db_mapper):
    start_tables_map()
    yield sessionmaker(bind=in_real_db_mapper)
    clear_mappers()

# session usado nos testes
@pytest.fixture
#def session(session_factory_mysql_db_mapper):
#    return session_factory_mysql_db_mapper()
def session(session_factory_memory_db_mapper):
    return session_factory_memory_db_mapper()



