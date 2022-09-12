from dependency_injector import containers, providers

from manutencao.solicitacao.api.Controllers.SolicitacaoDeManutencaoController import \
    solicitacao_de_manutencao_controller
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Services.AnaliseDeAprovacaoDaSolicitacaoDeManutencao import \
    AnaliseDeAprovacaoDaSolicitacaoDeManutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Fabricas.FabricaDeSolicitacaoDeManutencao import \
    FabricaDeSolicitacaoDeManutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Services.SolicitadorDeManutencao import SolicitadorDeManutencao
from manutencao.solicitacao.aplicacao.UnitOfWork import UnitOfWork
from manutencao.solicitacao.bootstrap.bootstrap import BootStrap
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.CanceladorDeSolicitacoesDeManutencaoPendentes import \
    CanceladorDeSolicitacoesDeManutencaoPendentes
from manutencao.solicitacao.infra.BancoDeDados.Repositorio.SolicitacaoDeManutencaoRepositorio import \
    SolicitacaoDeManutencaoRepositorio
from manutencao.solicitacao.infra.BancoDeDados.Repositorio.SubsidiariaRepositorio import SubsidiariaRepositorio
from manutencao.solicitacao.infra.ContextoServico.NotificaContextoDeServico import NotificaContextoDeServico
from manutencao.solicitacao.infra.Email.NotificaReprovacaoParaSolicitante import NotificaReprovacaoParaSolicitante
from manutencao.solicitacao.infra.ErpContratos.BuscadorDeContrato import BuscadorDeContrato


class Container(containers.DeclarativeContainer):

    # setup all our dependencies
    session = BootStrap(True)

    unit_of_work = providers.Singleton(
        UnitOfWork,
        session_factory=session,
        repositories=[SolicitacaoDeManutencaoRepositorio,
                      SubsidiariaRepositorio]
    )

    buscador_de_contrato = providers.Factory(
        BuscadorDeContrato,
        endereco="http://localhost:3000/contracts",
    )

    fabrica_de_solicitacao_de_manutencao = providers.Factory(
        FabricaDeSolicitacaoDeManutencao,
        uow=unit_of_work,
        buscador_de_contrato=buscador_de_contrato,
    )

    cancelador_de_solicitacoes_de_manutencao_pendentes = providers.Factory(
        CanceladorDeSolicitacoesDeManutencaoPendentes,
    )

    solicitador_de_manutencao = providers.Factory(
        SolicitadorDeManutencao,
        uow=unit_of_work,
        fabrica_de_solicitacao_de_manutencao=fabrica_de_solicitacao_de_manutencao,
        cancelador_de_solicitacoes_de_manutencao_pendentes=cancelador_de_solicitacoes_de_manutencao_pendentes,
    )

    notifica_reprovacao_para_solicitante = providers.Factory(
        NotificaReprovacaoParaSolicitante,
    )

    notifica_contexto_servico = providers.Factory(
        NotificaContextoDeServico,
    )

    analisador_da_solicitacao = providers.Factory(
        AnaliseDeAprovacaoDaSolicitacaoDeManutencao,
        uow=unit_of_work,
        notifica_reprovacao_para_solicitante=notifica_reprovacao_para_solicitante,
        notifica_contexto_servico=notifica_contexto_servico,
    )

    controller = providers.Factory(
        solicitacao_de_manutencao_controller,
        uow=unit_of_work,
        solicitador=solicitador_de_manutencao,
        analisador=analisador_da_solicitacao,
    )


def injector(app=None, request=None):

    container = Container()

    container.controller(app=app, request=request)





