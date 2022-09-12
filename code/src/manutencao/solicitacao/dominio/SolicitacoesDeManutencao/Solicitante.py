from typing import Optional

from manutencao.solicitacao.dominio.DomainException import DomainException
from utils.validators.Flunt import Flunt


class Solicitante:

    def __init__(self,
                 identificador: int,
                 nome: str):

        DomainException.lancar_quando(not Flunt.has_value(nome), "Nome do solicitante é inválido")

        self.identificador = identificador
        self.nome = nome

    def __composite_values__(self):
        return self.identificador, self.nome
