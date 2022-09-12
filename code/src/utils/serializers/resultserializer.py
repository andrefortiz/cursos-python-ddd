from utils.serializers.Serializer import Serializer


class ResultSerializer(Serializer):

    def __init__(self,
                 message, success, data, error=None):
        self.message = message
        self.success = success
        self.data = data
        self.error = error
