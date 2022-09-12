from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos import SolicitacaoDeManutencaoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Fabricas import FabricaDeSolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.ICanceladorDeSolicitacoesDeManutencaoPendentes import \
    ICanceladorDeSolicitacoesDeManutencaoPendentes
from utils.interfaces.IUnitOfWork import IUnitOfWork


class SolicitadorDeManutencao:

    def __init__(self,
                 uow: IUnitOfWork,
                 fabrica_de_solicitacao_de_manutencao: FabricaDeSolicitacaoDeManutencao,
                 cancelador_de_solicitacoes_de_manutencao_pendentes:
                    ICanceladorDeSolicitacoesDeManutencaoPendentes):

        self.uow = uow
        self.fabrica_de_solicitacao_de_manutencao = fabrica_de_solicitacao_de_manutencao
        self.cancelador_de_solicitacoes_de_manutencao_pendentes = cancelador_de_solicitacoes_de_manutencao_pendentes

    def solicitar(self, dto: SolicitacaoDeManutencaoDto = None):

        with self.uow:
            solicitacao_de_manutencao = self.fabrica_de_solicitacao_de_manutencao.fabricar(dto)

            solicitacoes_pendentes = self.uow.repository.obter_pendentes_do_tipo(
                solicitacao_de_manutencao.tipo_de_solicitacao_de_manutencao,
                solicitacao_de_manutencao.identificador_da_subsidiaria
            )

            self.cancelador_de_solicitacoes_de_manutencao_pendentes.cancelar(solicitacoes_pendentes)

            self.uow.repository.add(solicitacao_de_manutencao)
            self.uow.commit()
