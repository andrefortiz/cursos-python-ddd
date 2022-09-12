import datetime

from utils.interfaces.IDto import IDto


class SolicitacaoDeManutencaoDto(IDto):

    def __init__(self,
                 subsidiaria_id: str = None,
                 solicitante_id: int = None,
                 nome_do_solicitante: str = None,
                 tipo_de_solicitacao_de_manutencao: int = None,
                 justificativa: str = None,
                 numero_do_contrato: str = None,
                 inicio_desejado_para_manutencao: datetime = None):

        self.subsidiaria_id = subsidiaria_id
        self.solicitante_id = solicitante_id
        self.nome_do_solicitante = nome_do_solicitante
        self.tipo_de_solicitacao_de_manutencao = tipo_de_solicitacao_de_manutencao
        self.justificativa = justificativa
        self.numero_do_contrato = numero_do_contrato
        self.inicio_desejado_para_manutencao = inicio_desejado_para_manutencao
