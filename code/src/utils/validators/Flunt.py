import re


class Flunt:
    errors = []

    def __init__(self):
        self.errors = []

    def is_required(self, value, message):
        if value is None or (isinstance(value, str) and len(value.strip()) == 0):
            self.errors.append(message)

    def has_min_len(self, value, min, message):
        if value is None or (isinstance(value, str) and len(value) < min):
            self.errors.append(message)

    def has_max_len(self, value, max, message):
        if value is None or (isinstance(value, str) and len(value) > max):
            self.errors.append(message)

    def has_fixed_len(self, value, len, message):
        if value is None or (isinstance(value, str) and len(value) != len):
            self.errors.append(message)

    def is_granter_than(self, value, max, message):
        if value is None or value > max:
            self.errors.append(message)

    def is_email(self, value, message):
        #r = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
        r = re.compile(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
        if not r.match(value):
            self.errors.append(message)

    def clear(self):
        self.errors = []

    def is_valid(self):
        return len(self.errors) == 0

    @staticmethod
    def has_value(value):
        if value is None or (isinstance(value, str) and len(value.strip()) == 0):
            return False
        return True
