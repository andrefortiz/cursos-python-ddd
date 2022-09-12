from manutencao.solicitacao.api.contracts.AnaliseDeAprovacaoContract import AnaliseDeAprovacaoContract
from manutencao.solicitacao.api.contracts.SolicitacaoDeManutencaoContract import SolicitacaoDeManutencaoContract
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.AnaliseDeAprovacaoDto import AnaliseDeAprovacaoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.SolicitacaoDeManutencaoDto import \
    SolicitacaoDeManutencaoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Services import SolicitadorDeManutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Services.AnaliseDeAprovacaoDaSolicitacaoDeManutencao \
    import AnaliseDeAprovacaoDaSolicitacaoDeManutencao
from utils.interfaces.IUnitOfWork import IUnitOfWork
from utils.responses.Responses import ResponseCreated, ResponseError, ResponseNotFound, ResponseSuccess, \
    ResponseAccepted
from utils.serializers.AnonType import AnonType
from utils.serializers.serializer import Serializer
from utils.validators.ValidatorInterceptor import validator_interceptor


def solicitacao_de_manutencao_controller(
        uow: IUnitOfWork,
        solicitador: SolicitadorDeManutencao,
        analisador: AnaliseDeAprovacaoDaSolicitacaoDeManutencao,
        app, request):

    @app.route("/api/solicitador-de-manutencao", methods=['POST'])
    @validator_interceptor(SolicitacaoDeManutencaoContract(SolicitacaoDeManutencaoDto), request)
    def solicitador_de_manutencao(dto):
        try:
            solicitador.solicitar(dto)

            return ResponseCreated()
        except Exception as e:
            return ResponseError(error=str(e))

    @app.route("/api/analise", methods=['PUT'])
    @validator_interceptor(AnaliseDeAprovacaoContract(AnaliseDeAprovacaoDto), request)
    def analisar(dto):
        try:
            analisador.analisar(dto)

            return ResponseAccepted(message="Analise realizada com sucesso.")
        except Exception as e:
            return ResponseError(error=str(e))

    @app.route("/api/pendentes/<identificador_da_subsidiaria>")
    def listar_pendentes(identificador_da_subsidiaria):
        try:

            with uow:

                query_result = uow.repository.obter_pendentes_da(
                    identificador_da_subsidiaria
                )

                if not query_result:
                    return ResponseNotFound()

                result = Serializer(
                    query_result,
                    lambda solicitacao: AnonType(
                        id=solicitacao.id,
                        data_da_solicitacao=solicitacao.data_da_solicitacao,
                        justificativa=solicitacao.justificativa,
                        nome_do_solicitante=solicitacao.solicitante.nome,
                        contrato=solicitacao.contrato.numero,
                        inicio_desejado=solicitacao.inicio_desejado_para_manutencao,
                        tipo_de_solicitacao=solicitacao.tipo_de_solicitacao_de_manutencao
                    )
                ).to_list()

                return ResponseSuccess(data=result)
            return ResponseNotFound()
        except Exception as e:
            return ResponseError(error=str(e))


