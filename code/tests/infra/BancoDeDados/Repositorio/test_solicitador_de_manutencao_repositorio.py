from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from manutencao.solicitacao.infra.BancoDeDados.Repositorio.SolicitacaoDeManutencaoRepositorio import \
    SolicitacaoDeManutencaoRepositorio
from utils.types.DateTime import DateTime

def create():
    id_subsidiaria = "XPT-TO"
    id_solicitante = 1
    nome_solicitante = "CASSIA"
    justificativa = "teste"
    numero_do_contrato = "XPTO=33"
    inicio_desejado_para_manutencao = DateTime.add_days(10)

    solicitacao = SolicitacaoDeManutencao(id_subsidiaria,
                                          id_solicitante,
                                          nome_solicitante,
                                          TipoDeSolicitacaoDeManutencao.Jardinagem,
                                          justificativa,
                                          numero_do_contrato,
                                          "ANDRE CNPJ",
                                          "99999999999999",
                                          "ANDRE",
                                          DateTime.add_days(180),
                                          inicio_desejado_para_manutencao, )

    return solicitacao

def test_get_by_id_solicitacao(session):

    repo = SolicitacaoDeManutencaoRepositorio(session)

    solicitacao = create()

    repo.add(solicitacao)

    # usar para criar as subsidiarias na base de dados
    #session.commit()

    retorno = repo.get(solicitacao.id)

    assert retorno.id == solicitacao.id\
           and retorno.contrato.gestor_do_contrato == solicitacao.contrato.gestor_do_contrato
