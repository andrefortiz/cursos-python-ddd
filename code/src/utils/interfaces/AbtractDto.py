
class AbstractDto:
    @classmethod
    def from_json(cls, data):
        return cls(**data)
