import json

from utils.interfaces.IContract import AbstractContract
from utils.validators.Flunt import Flunt


class SubsidiariaContract(AbstractContract):
    request = None
    domain_class = None

    def __init__(self, domain_class):
        super().__init__(domain_class)

    def validate(self, request):
        if Flunt.has_value(request) and Flunt.has_value(request.data):
            data = self.domain_class.from_json(json.loads(request.data))
            flunt = Flunt()

            if flunt.has_value(data):
                flunt.has_min_len(data.nome_cidade, 3, 'O nome da cidade deve conter no minimo 3 caracteres')

            self.errors = flunt.errors
        return data

