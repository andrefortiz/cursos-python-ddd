import unittest
from unittest.mock import patch

from dominio.SolicitacoesDeManutencao.test_solicitacao_de_manutencao import test_solicitacao_de_manutencao
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.ISolicitacaoDeManutencaoRepositorio import \
    ISolicitacaoDeManutencaoRepositorio

from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.CanceladorDeSolicitacoesDeManutencaoPendentes import \
    CanceladorDeSolicitacoesDeManutencaoPendentes
from manutencao.solicitacao.dominio.SolicitacoesDeManutencao.StatusDaSolicitacao import StatusDaSolicitacao


class test_cancelador_de_solicitacao_de_manutencao(unittest.TestCase):

    @patch.object(ISolicitacaoDeManutencaoRepositorio, 'obter_pendentes_do_tipo')
    def test_deve_cancelar_solicitacoes_de_manutencao_pendentes_para_o_tipo_e_subsidiaria(
            self,

            mock_obter_pendentes_do_tipo
    ):
        solicitacoes_pendente = [
            test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao(),
            test_solicitacao_de_manutencao.criar_solicitacao_de_manutencao(),
        ]

        mock_obter_pendentes_do_tipo.return_value = solicitacoes_pendente

        cancelador = CanceladorDeSolicitacoesDeManutencaoPendentes()

        cancelador.cancelar(solicitacoes_pendente)

        assert solicitacoes_pendente[0].status_da_solicitacao == StatusDaSolicitacao.Cancelada
        assert solicitacoes_pendente[1].status_da_solicitacao == StatusDaSolicitacao.Cancelada

    def test_nao_deve_lancar_excecao_quando_solicitacoes_de_manutecao_for_nula(self):

        cancelador = CanceladorDeSolicitacoesDeManutencaoPendentes()

        cancelador.cancelar(None)
