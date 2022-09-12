from sqlalchemy import (
    MetaData
)


from manutencao.solicitacao.infra.BancoDeDados.Tabelas.SolicitacaoDeManutencaoTabela import \
    SolicitacaoDeManutencaoTabela
from manutencao.solicitacao.infra.BancoDeDados.Tabelas.SubsidiariaTabela import SubsidiariaTabela

metadata = MetaData()

solicitacao_de_manutencao_tabela = SolicitacaoDeManutencaoTabela.create_table(metadata)
subsidiaria_tabela = SubsidiariaTabela.create_table(metadata)


def start_tables_map():

    solicitacao_de_manutencao_mapper = SolicitacaoDeManutencaoTabela.create_mapper(solicitacao_de_manutencao_tabela)

    subsidiaria_mapper = SubsidiariaTabela.create_mapper(subsidiaria_tabela)



