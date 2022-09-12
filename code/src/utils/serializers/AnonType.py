class AnonType(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__