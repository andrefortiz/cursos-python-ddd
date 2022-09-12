from utils.interfaces.IUnitOfWork import IUnitOfWork
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao import SolicitacaoDeManutencaoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.IBuscadorDeContrato import \
    IBuscadorDeContrato
from manutencao.solicitacao.aplicacao.Subsidiarias.ISubsidiariaRepositorio import ISubsidiariaRepositorio
from manutencao.solicitacao.dominio.DomainException import DomainException
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao


class FabricaDeSolicitacaoDeManutencao:

    def __init__(self,
                 uow: IUnitOfWork,
                 #subsidiaria_repositorio: ISubsidiariaRepositorio,
                 buscador_de_contrato: IBuscadorDeContrato):

        self.uow = uow
        #self.subsidiaria_repositorio = subsidiaria_repositorio
        self.buscador_de_contrato = buscador_de_contrato

    def fabricar(self, dto: SolicitacaoDeManutencaoDto) -> SolicitacaoDeManutencao:
        # apenas temporario ate melhorar a implementacao da injecao dos repositorios
        # e do unit_of_work com a mesma sessoo
        with self.uow:
            #self.subsidiaria_repositorio.set_session(self.uow.get_session())

            subsidiaria = self.uow.subsidiaria_repositorio.get(dto.subsidiaria_id)
            DomainException.lancar_quando(subsidiaria is None,
                                          "Subsidiária é inválida")

            contrato_dto = self.buscador_de_contrato.buscar(dto.numero_do_contrato)
            DomainException.lancar_quando(contrato_dto is None,
                                          "Contrato não encontrado no ERP")

            tipo_de_solicitacao_de_manutencao = TipoDeSolicitacaoDeManutencao(dto.tipo_de_solicitacao_de_manutencao)

            return SolicitacaoDeManutencao(
                subsidiaria.id,
                dto.solicitante_id,
                dto.nome_do_solicitante,
                tipo_de_solicitacao_de_manutencao,
                dto.justificativa,
                contrato_dto.numero,
                contrato_dto.nome_da_terceirizada,
                contrato_dto.cnpf_da_terceirizada,
                contrato_dto.gestor_do_contrato,
                contrato_dto.data_final_da_vigencia,
                dto.inicio_desejado_para_manutencao
            )

