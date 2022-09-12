import requests

from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Dtos.ContratoDto import ContratoDto
from manutencao.solicitacao.aplicacao.SolicitacoesDeManutencao.Interfaces.IBuscadorDeContrato import \
    IBuscadorDeContrato
from utils.types.DateTime import Date


class BuscadorDeContrato(IBuscadorDeContrato):

    def __init__(self, endereco):
        self.endereco = endereco

    def buscar(self,
               numero: str) -> ContratoDto:

        try:
            response = requests.get("{}/{}".format(self.endereco, numero))

            return ContratoDto(
                numero=response.json()['id'],
                nome_da_terceirizada=response.json()['company'],
                cnpf_da_terceirizada=response.json()['companyid'],
                gestor_do_contrato=response.json()['manager'],
                data_final_da_vigencia=Date.convert_to_date(response.json()['finaldate']),
            )

            # Additional code will only run if the request is successful
        except requests.exceptions.HTTPError as e:
            return None



