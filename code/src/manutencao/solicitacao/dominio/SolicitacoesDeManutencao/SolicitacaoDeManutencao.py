import datetime

from manutencao.solicitacao.dominio.AbstractEntity import AbstractEntity
from utils.interfaces.IEntity import IEntity
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Contrato import Contrato
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Autor import Autor
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.StatusDaSolicitacao import StatusDaSolicitacao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from utils.validators.Flunt import Flunt


class SolicitacaoDeManutencao(AbstractEntity, IEntity):

    aprovador = None

    def __init__(self,
                 identificador_da_subsidiaria: str,
                 identificador_do_solicitante: int,
                 nome_do_solicitante: str,
                 tipo_de_solicitacao_de_manutencao: TipoDeSolicitacaoDeManutencao,
                 justificativa: str,
                 numero_do_contrato: str,
                 nome_da_terceirizada: str,
                 cnpj_da_terceirizada: str,
                 gestor_do_contrato: str,
                 data_final_da_vigencia: datetime,
                 inicio_desejado_para_manutencao: datetime):
        super().__init__()
        DomainException.lancar_quando(not Flunt.has_value(identificador_da_subsidiaria), "Subsidiária é inválida")
        DomainException.lancar_quando(not Flunt.has_value(justificativa), "Justificativa inválida")
        DomainException.lancar_quando(not Flunt.has_value(inicio_desejado_para_manutencao),
                                      "Inicio desejado para manutenção inválido")
        DomainException.lancar_quando(inicio_desejado_para_manutencao < datetime.datetime.now(),
                                      "Data inicio desejado para manutenção deve ser maior que data atual")

        self.solicitante = Autor(identificador_do_solicitante, nome_do_solicitante)
        self.identificador_da_subsidiaria = identificador_da_subsidiaria
        self.tipo_de_solicitacao_de_manutencao = tipo_de_solicitacao_de_manutencao
        self.justificativa = justificativa
        self.contrato = Contrato(numero_do_contrato, nome_da_terceirizada,
                                 cnpj_da_terceirizada, gestor_do_contrato, data_final_da_vigencia)
        self.inicio_desejado_para_manutencao = inicio_desejado_para_manutencao
        self.data_da_solicitacao = datetime.datetime.now()
        self.status_da_solicitacao = StatusDaSolicitacao.Pendente

        self.aprovador = Autor(0, "Sem aprovador")

    def cancelar(self):
        self.status_da_solicitacao = StatusDaSolicitacao.Cancelada

    def reprovar(self, aprovador: Autor):
        self.aprovador = aprovador
        self.status_da_solicitacao = StatusDaSolicitacao.Reprovada

    def aprovar(self, aprovador: Autor):
        self.aprovador = aprovador
        self.status_da_solicitacao = StatusDaSolicitacao.Aprovada
