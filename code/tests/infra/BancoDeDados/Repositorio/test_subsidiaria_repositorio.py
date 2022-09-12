from manutencao.solicitacao.dominio.Subsidiarias.Subsidiaria import Subsidiaria
from manutencao.solicitacao.infra.BancoDeDados.Repositorio.SubsidiariaRepositorio import SubsidiariaRepositorio


def create(nome):
    subsidiaria = Subsidiaria(nome)

    return subsidiaria

def test_get_by_id_subsidiaria(session):

    repo = SubsidiariaRepositorio(session)

    subsidiaria = create("BRASIL")

    repo.add(subsidiaria)

    #usar para criar as subsidiarias na base de dados
    #session.commit()

    retorno = repo.get(subsidiaria.id)

    assert retorno.id == subsidiaria.id and retorno.nome == subsidiaria.nome