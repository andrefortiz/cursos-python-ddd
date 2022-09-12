import enum


class StatusDaSolicitacao(enum.IntEnum):
    Pendente = 1
    Cancelada = 2
    Reprovada = 3
    Aprovada = 4

    def describe(self):
        return lambda: 'Pendente' if self.value == 1 else 'Cancelada'



