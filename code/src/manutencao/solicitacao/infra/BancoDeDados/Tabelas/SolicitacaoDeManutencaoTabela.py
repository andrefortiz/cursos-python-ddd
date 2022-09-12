from sqlalchemy import Table, Column, String, Integer, DateTime
from sqlalchemy.orm import mapper, composite

from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Contrato import Contrato
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Autor import Autor
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.StatusDaSolicitacao import StatusDaSolicitacao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from utils.types.SmallintEnum import SmallIntEnum


class SolicitacaoDeManutencaoTabela:
    @staticmethod
    def create_table(metadata):
        return Table(
            'solicitacao_manutencao', metadata,
            Column('ID', String(36), primary_key=True),
            Column('ID_SOLICITANTE', Integer, nullable=False),
            Column('NOME_SOLICITANTE', String(255), nullable=False),
            Column('ID_SUBSIDIARIA', String(36), nullable=False),
            Column('TIPO', SmallIntEnum(TipoDeSolicitacaoDeManutencao), nullable=False),
            Column('JUSTIFICATIVA', String(255), nullable=False),
            Column('ID_CONTRATO', String(36), nullable=False),
            Column('NOME_TERCEIRAZADA', String(255), nullable=False),
            Column('CNPJ_TERCEIRAZADA', String(14), nullable=False),
            Column('GESTOR_CONTRATO', String(255), nullable=False),
            Column('DT_FIM_VIGENCIA', DateTime(), nullable=False),
            Column('STATUS', SmallIntEnum(StatusDaSolicitacao), nullable=False),
            Column('DT_INICIO_DESEJADO', DateTime()),
            Column('DT_SOLICITACAO', DateTime()),
            Column('ID_APROVADOR', Integer),
            Column('NOME_APROVADOR', String(255)),

        )

    @staticmethod
    def create_mapper(table):
        return mapper(SolicitacaoDeManutencao, table, properties={
            'id': table.c.ID,
            'solicitante': composite(
                Autor,
                table.c.ID_SOLICITANTE,
                table.c.NOME_SOLICITANTE),
            'tipo_de_solicitacao_de_manutencao': table.c.TIPO,
            'justificativa': table.c.JUSTIFICATIVA,
            'status_da_solicitacao': table.c.STATUS,
            'identificador_da_subsidiaria': table.c.ID_SUBSIDIARIA,
            'inicio_desejado_para_manutencao': table.c.DT_INICIO_DESEJADO,
            'data_da_solicitacao': table.c.DT_SOLICITACAO,
            'contrato': composite(
                Contrato,
                table.c.ID_CONTRATO,
                table.c.NOME_TERCEIRAZADA,
                table.c.CNPJ_TERCEIRAZADA,
                table.c.GESTOR_CONTRATO,
                table.c.DT_FIM_VIGENCIA,),
            'aprovador': composite(
                Autor,
                table.c.ID_APROVADOR,
                table.c.NOME_APROVADOR),
            '_id_solicitante': table.c.ID_SOLICITANTE,
            '_nome_solicitante': table.c.NOME_SOLICITANTE,
            '_id_contrato': table.c.ID_CONTRATO,
            '_nome_terceirizada': table.c.NOME_TERCEIRAZADA,
            '_cnpj_terceirizada': table.c.CNPJ_TERCEIRAZADA,
            '_gestor_contrato': table.c.GESTOR_CONTRATO,
            '_dt_fim_vigencia': table.c.DT_FIM_VIGENCIA,
            '_id_aprovador': table.c.ID_APROVADOR,
            '_nome_aprovador': table.c.NOME_APROVADOR,

        })