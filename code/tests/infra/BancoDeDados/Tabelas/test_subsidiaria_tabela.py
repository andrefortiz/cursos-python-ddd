from manutencao.solicitacao.dominio.Subsidiarias.Subsidiaria import Subsidiaria


def add_subsidiaria(session_test):
    nome = "MONTEVIDEO"

    subsidiaria = Subsidiaria(nome)
    session_test.add(subsidiaria)
    session_test.flush()

    rows = list(session_test.execute('SELECT  '
                                     'ID, '
                                     'NOME_SUBSIDIARIA '
                                     'FROM subsidiaria WHERE NOME_SUBSIDIARIA=:nome_subsidiaria',
                                     dict(nome_subsidiaria=nome)))

    assert rows == [(
        subsidiaria.id, subsidiaria.nome
    )]
    return subsidiaria


def test_deve_salvar_subsidiaria(session):
    add_subsidiaria(session)






