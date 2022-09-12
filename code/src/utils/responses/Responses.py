from utils.serializers.Result import Result
from utils.serializers.Serializer import Serializer
from http import HTTPStatus


class ResponseBase:
    def __new__(cls, result, status, headers):

        return result, status, headers

    @staticmethod
    def get_params(**kwargs):
        headers = {}
        content_type = 'application/Json'
        return_status = None

        if 'content_type' in kwargs:
            content_type = kwargs['content_type']
        if 'status' in kwargs:
            return_status = kwargs['status']

        headers['Content-Type'] = content_type

        return return_status, headers

    @staticmethod
    def get_result(success, default_message, **kwargs):
        data = None
        error = None
        message = default_message

        if len(kwargs) > 0:
            if 'message' in kwargs:
                message = kwargs['message']
            if 'data' in kwargs:
                data = kwargs['data']
            if 'error' in kwargs:
                error = kwargs['error']

        if isinstance(data, Serializer):
            data = data.serialize()
        if isinstance(data, list):
            item = data[0]
            if isinstance(item, Serializer):
                data = item.serialize_list(data)

        return Result(message, data, success, error)


class ResponseCreated(ResponseBase):
    def __new__(cls, **kwargs):
        return_status, headers = super().get_params(**kwargs)
        return_status = HTTPStatus.CREATED if return_status is None else return_status

        default_message = "Cadastro realizado com sucesso"
        result = super().get_result(True, default_message, **kwargs)
        return super().__new__(cls, result.to_json(), return_status, headers)


class ResponseAccepted(ResponseBase):
    def __new__(cls, **kwargs):
        return_status, headers = super().get_params(**kwargs)
        return_status = HTTPStatus.ACCEPTED if return_status is None else return_status

        default_message = "Atualização realizada com sucesso"
        result = super().get_result(True, default_message, **kwargs)
        return super().__new__(cls, result.to_json(), return_status, headers)


class ResponseSuccess(ResponseBase):
    def __new__(cls, **kwargs):
        return_status, headers = super().get_params(**kwargs)
        return_status = HTTPStatus.OK if return_status is None else return_status

        message = "Requisição realizada com sucesso"
        result = super().get_result(True, message, **kwargs)
        return super().__new__(cls, result.to_json(), return_status, headers)


class ResponseNotFound(ResponseBase):
    def __new__(cls, **kwargs):
        return_status, headers = super().get_params(**kwargs)
        return_status = HTTPStatus.NOT_FOUND if return_status is None else return_status

        default_message = "Nenhum registro encontrado"
        result = super().get_result(False, default_message, **kwargs)
        return super().__new__(cls, result.to_json(), return_status, headers)


class ResponseError(ResponseBase):
    def __new__(cls, **kwargs):
        return_status, headers = super().get_params(**kwargs)
        return_status = HTTPStatus.BAD_REQUEST if return_status is None else return_status

        default_message = "Ocorreu erro inesperado"
        result = super().get_result(False, default_message, **kwargs)
        return super().__new__(cls, result.to_json(), return_status, headers)


class ResponseForbiden(ResponseBase):
    def __new__(cls, **kwargs):
        return_status, headers = super().get_params(**kwargs)
        return_status = HTTPStatus.FORBIDDEN if return_status is None else return_status

        default_message = "Requisição proibida"
        result = super().get_result(False, default_message, **kwargs)
        return super().__new__(cls, result.to_json(), return_status, headers)


class Response(ResponseBase):
    def __new__(cls, status: HTTPStatus, message: str, **kwargs):

        return_status, headers = super().get_params(**kwargs)
        return_status = status

        result = super().get_result(False, message, **kwargs)
        return super().__new__(cls, result.to_json(), return_status, headers)
