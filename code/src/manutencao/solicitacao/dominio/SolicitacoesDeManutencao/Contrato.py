import datetime

from manutencao.solicitacao.dominio.DomainException import DomainException
from utils.validators.Flunt import Flunt


class Contrato:

    def __init__(self,
                 numero: str,
                 nome_da_terceirizada: str,
                 cnpj_da_terceirizada: str,
                 gestor_do_contrato: str,
                 data_final_da_vigencia: datetime):

        DomainException.lancar_quando(not Flunt.has_value(numero), "Número do contrato é inválido")
        DomainException.lancar_quando(not Flunt.has_value(nome_da_terceirizada), "Nome da terceirizada é inválido")
        DomainException.lancar_quando(not Flunt.has_value(cnpj_da_terceirizada) or
                                      len(cnpj_da_terceirizada.strip()) < 14,
                                      "CNPJ da terceirizada é inválido")
        DomainException.lancar_quando(not Flunt.has_value(gestor_do_contrato), "Gestor do contrato é inválido")
        DomainException.lancar_quando(data_final_da_vigencia < datetime.datetime.now(),
                                      "Vigência do contrato esta vencido")

        self.numero = numero
        self.nome_da_terceirizada = nome_da_terceirizada
        self.cnpj_da_terceirizada = cnpj_da_terceirizada
        self.gestor_do_contrato = gestor_do_contrato
        self.data_final_da_vigencia = data_final_da_vigencia

    def __composite_values__(self):
        #tem que ter a virgula se não ele corta o valor da variavel deixando 1 posicao apenas.
        return self.numero, self.nome_da_terceirizada, self.cnpj_da_terceirizada, self.gestor_do_contrato, \
               self.data_final_da_vigencia
