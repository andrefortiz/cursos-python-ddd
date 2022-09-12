from utils.interfaces.IUnitOfWork import IUnitOfWork
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao import SolicitacaoDeManutencaoDto, \
    FabricaDeSolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.ICanceladorDeSolicitacoesDeManutencaoPendentes import \
    ICanceladorDeSolicitacoesDeManutencaoPendentes


class SolicitadorDeManutencao:

    def __init__(self,
                 uow: IUnitOfWork,
                 #solicitacao_de_manutencao_repositorio: ISolicitacaoDeManutencaoRepositorio,
                 fabrica_de_solicitacao_de_manutencao: FabricaDeSolicitacaoDeManutencao,
                 cancelador_de_solicitacoes_de_manutencao_pendentes:
                    ICanceladorDeSolicitacoesDeManutencaoPendentes):

        self.uow = uow
        #self.solicitacao_de_manutencao_repositorio = solicitacao_de_manutencao_repositorio
        self.fabrica_de_solicitacao_de_manutencao = fabrica_de_solicitacao_de_manutencao
        self.cancelador_de_solicitacoes_de_manutencao_pendentes = cancelador_de_solicitacoes_de_manutencao_pendentes

    def solicitar(self, dto: SolicitacaoDeManutencaoDto = None):
        # apenas temporario ate melhorar a implementacao da injecao dos repositorios
        # e do unit_of_work com a mesma sessoo
        #self.solicitacao_de_manutencao_repositorio.set_session(self.uow.get_session())
        with self.uow:
            solicitacao_de_manutencao = self.fabrica_de_solicitacao_de_manutencao.fabricar(dto)

            solicitacoes_pendentes = self.uow.repository.obter_pendentes_do_tipo(
                solicitacao_de_manutencao.tipo_de_solicitacao_de_manutencao,
                solicitacao_de_manutencao.identificador_da_subsidiaria
            )

            self.cancelador_de_solicitacoes_de_manutencao_pendentes.cancelar(solicitacoes_pendentes)

            self.uow.repository.add(solicitacao_de_manutencao)
            self.uow.commit()
