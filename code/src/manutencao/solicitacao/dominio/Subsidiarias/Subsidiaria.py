from manutencao.solicitacao.dominio.AbstractEntity import AbstractEntity
from utils.interfaces.IEntity import IEntity
from manutencao.solicitacao.dominio.DomainException import DomainException
from utils.validators.Flunt import Flunt


class Subsidiaria(AbstractEntity, IEntity):

    def __init__(self, nome, **kwargs):
        super().__init__(**kwargs)
        DomainException.lancar_quando(not Flunt.has_value(nome), "Nome da subsidiária é inválido")

        self.nome = nome
