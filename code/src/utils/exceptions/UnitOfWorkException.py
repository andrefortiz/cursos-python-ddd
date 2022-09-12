

class UnitOfWorkException(Exception):
    pass

    @staticmethod
    def lancar_quando(regra_invalida, mensagem):
        if regra_invalida:
            raise UnitOfWorkException(mensagem)
