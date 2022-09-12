import json

from utils.interfaces.IContract import IContract
from utils.serializers.Deserializer import Deserializer
from utils.validators.AbstractContract import AbstractContract
from utils.validators.Flunt import Flunt


class AnaliseDeAprovacaoContract(AbstractContract, IContract):
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
                flunt.is_required(data.identificador_do_aprovador, 'Identificador do aprovador não informado')
                flunt.is_required(data.nome_do_aprovador, 'Nome do aprovador não informado')
                flunt.is_required(data.id_da_solicitacao, 'Idenfificador da solicitação não informado')
                flunt.is_required(data.aprovado, 'A aprovação ou reprovação da solicitação não foi informado')

            self.errors = flunt.errors
        return data

