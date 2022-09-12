from utils.interfaces.IUnitOfWork import IUnitOfWork
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.ISolicitacaoDeManutencaoRepositorio import \
    ISolicitacaoDeManutencaoRepositorio
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.AnaliseDeAprovacaoDto import AnaliseDeAprovacaoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.INotificaContextoDeServico import \
    INotificaContextoDeServico
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.INotificaReprovacaoParaSolicitante import \
    INotificaReprovacaoParaSolicitante
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.Autor import Autor
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.StatusDaSolicitacao import StatusDaSolicitacao


class AnaliseDeAprovacaoDaSolicitacaoDeManutencao:

    def __init__(self,
                 uow: IUnitOfWork,
                 #solicitacao_de_manutencao_repositorio: ISolicitacaoDeManutencaoRepositorio,
                 notifica_reprovacao_para_solicitante: INotificaReprovacaoParaSolicitante,
                 notifica_contexto_servico: INotificaContextoDeServico):

        self.uow = uow
        #self.solicitacao_de_manutencao_repositorio = solicitacao_de_manutencao_repositorio
        self.notifica_reprovacao_para_solicitante = notifica_reprovacao_para_solicitante
        self.notifica_contexto_servico = notifica_contexto_servico

    def analisar(self, dto: AnaliseDeAprovacaoDto):

        # apenas temporario ate melhorar a implementacao da injecao dos repositorios
        # e do unit_of_work com a mesma sessoo
        #self.solicitacao_de_manutencao_repositorio.set_session(self.uow.get_session())
        with self.uow:
            solicitacao = self.uow.repository.get(reference=dto.id_da_solicitacao)
            DomainException.lancar_quando(solicitacao is None, "Solicitação não encontrada")
            DomainException.lancar_quando(solicitacao.status_da_solicitacao == StatusDaSolicitacao.Reprovada,
                                      "Solicitação já analisada e reprovada.")
            DomainException.lancar_quando(solicitacao.status_da_solicitacao == StatusDaSolicitacao.Aprovada,
                                      "Solicitação já analisada e aprovada.")

            if not dto.aprovado:
                solicitacao.reprovar(Autor(dto.identificador_do_aprovador, dto.nome_do_aprovador))
                self.notifica_reprovacao_para_solicitante.notificar(solicitacao)
            else:
                solicitacao.aprovar(Autor(dto.identificador_do_aprovador, dto.nome_do_aprovador))
                self.notifica_contexto_servico.notificar(solicitacao)
            self.uow.commit()

