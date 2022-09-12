from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.SolicitacaoDeManutencao import SolicitacaoDeManutencao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.StatusDaSolicitacao import StatusDaSolicitacao
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.TipoDeSolicitacaoDeManutencao import \
    TipoDeSolicitacaoDeManutencao
from utils.types.DateTime import DateTime


def add_solicitacao_de_manutecao(session_test):
    id_subsidiaria="XPT-TO"
    id_solicitante=1
    nome_solicitante="CASSIA"
    justificativa="teste"
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
                                          inicio_desejado_para_manutencao,)
    session_test.add(solicitacao)
    session_test.flush()

    rows = list(session_test.execute('SELECT  '
                                     'ID, '
                                     'ID_SOLICITANTE, '
                                     'NOME_SOLICITANTE, '
                                     'ID_SUBSIDIARIA, '
                                     'TIPO, '
                                     'JUSTIFICATIVA, '
                                     'ID_CONTRATO, '
                                     'STATUS '
                                     'FROM solicitacao_manutencao WHERE ID_CONTRATO=:id_contrato',
                                     dict(id_contrato=numero_do_contrato)))

    assert rows == [(
        solicitacao.id, id_solicitante, nome_solicitante, id_subsidiaria,
        TipoDeSolicitacaoDeManutencao.Jardinagem.__hash__(), justificativa, numero_do_contrato,
        StatusDaSolicitacao.Pendente.__hash__(),
        #inicio_desejado_para_manutencao.strftime("%Y-%m-%d %H:%M:%S")
    )]
    return solicitacao


def test_deve_salvar_solicitacao_de_manutencao(session):
    add_solicitacao_de_manutecao(session)






