from sqlalchemy import Table, Column, String
from sqlalchemy.orm import mapper

from manutencao.solicitacao.dominio.Subsidiarias.Subsidiaria import Subsidiaria


class SubsidiariaTabela:
    @staticmethod
    def create_table(metadata):
        return Table(
            'subsidiaria', metadata,
            Column('ID', String(36), primary_key=True),
            Column('NOME_SUBSIDIARIA', String(255), nullable=False),
        )

    @staticmethod
    def create_mapper(table):
        return mapper(Subsidiaria, table, properties={
            'id': table.c.ID,
            'nome':  table.c.NOME_SUBSIDIARIA,
        })