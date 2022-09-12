import json

from utils.interfaces.IContract import IContract
from utils.serializers.Deserializer import Deserializer
from utils.validators.AbstractContract import AbstractContract
from utils.validators.Flunt import Flunt


class SolicitacaoDeManutencaoContract(AbstractContract, IContract):
    request = None
    dto_class = None

    def __init__(self, dto_class):
        super().__init__(dto_class)

    def validate(self, request):
        data = None
        if request is not None and Flunt.has_value(request.data):
            data = self.dto_class.from_json(json.loads(request.data, object_hook=Deserializer.date_parser))
            flunt = Flunt()

            if flunt.has_value(data):
                flunt.is_required(data.subsidiaria_id, 'Identificador da subsidiária não informado')
                flunt.is_required(data.solicitante_id, 'Identificador do solicitante não informado')
                flunt.is_required(data.nome_do_solicitante, 'Nome do solicitante não informado')
                flunt.is_required(data.numero_do_contrato, 'Número do contrato não informado')
                flunt.is_required(data.tipo_de_solicitacao_de_manutencao, 'Tipo de solicitação não informado')
                flunt.has_min_len(data.justificativa, 3, 'A justificativa deve conter no minimo 3 caracteres')

            self.errors = flunt.errors
        return data

