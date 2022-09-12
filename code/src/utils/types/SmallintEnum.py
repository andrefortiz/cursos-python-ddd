from sqlalchemy import types
import enum

class SmallIntEnum(types.TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """
    impl = types.SmallInteger

    def __init__(self, enumtype, *args, **kwargs):
        super(SmallIntEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, enum.IntEnum):
            return value.value
        if isinstance(value, int):
            return value
        elif value is None:
            return value
        return value.value

    def process_result_value(self, value, dialect):
        if value is not None:
            return self._enumtype(value)
        return value
