from utils.interfaces.IDto import IDto


class AnaliseDeAprovacaoDto(IDto):

    def __init__(self,
                 identificador_do_aprovador: int = None,
                 nome_do_aprovador: str = None,
                 id_da_solicitacao: str = None,
                 aprovado: bool = None):

        self.identificador_do_aprovador = identificador_do_aprovador
        self.nome_do_aprovador = nome_do_aprovador
        self.id_da_solicitacao = id_da_solicitacao
        self.aprovado = aprovado