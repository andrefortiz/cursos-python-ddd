import datetime

from utils.interfaces.IDto import IDto


class ContratoDto(IDto):

    def __init__(self,
                 numero: str,
                 nome_da_terceirizada: str,
                 cnpf_da_terceirizada: str,
                 gestor_do_contrato: str,
                 data_final_da_vigencia: datetime):

        self.numero = numero
        self.nome_da_terceirizada = nome_da_terceirizada
        self.cnpf_da_terceirizada = cnpf_da_terceirizada
        self.gestor_do_contrato = gestor_do_contrato
        self.data_final_da_vigencia = data_final_da_vigencia
