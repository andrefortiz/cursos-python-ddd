import os

from tenacity import retry, stop_after_delay

from manutencao.solicitacao.infra.BancoDeDados.metadata import metadata
from settings import BASE_DIR
from sqlalchemy import create_engine


@retry(stop=stop_after_delay(10))
def wait_for_mysql_to_come_up(engine):
    return engine.connect()


def get_mysql_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 6603 if host == 'localhost' else 3306
    password = os.environ.get('DB_PASSWORD', 'leg@1583')
    user, db_name = 'admin', 'ddd_mysql'
    return f"mysql://{user}:{password}@{host}:{port}/{db_name}"


def get_mysql_engine():
    engine = create_engine(get_mysql_uri(), isolation_level='SERIALIZABLE')
    wait_for_mysql_to_come_up(engine)
    metadata.create_all(engine)
    return engine


def get_sqlite_engine():
    engine = create_engine('sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
    metadata.create_all(engine)
    return engine


def get_sqlite_engine_memory():
    engine = create_engine('sqlite:///:memory:', echo=True)
    metadata.create_all(engine)
    return engine


def get_api_url(local: bool = False):
    host_string = '192.168.99.100'
    host_port = 80
    if local:
        host_string = '127.0.0.1'
        host_port = 5000
    host = os.environ.get('API_HOST', host_string)
    port = host_port if host == host_string else 80
    return f"http://{host}:{port}"

