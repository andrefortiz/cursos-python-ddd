import re

from pyparsing import basestring

from utils.types.DateTime import Date


class Deserializer(object):

    @staticmethod
    def date_parser(dct):
        for k, v in dct.items():
            if isinstance(v, basestring):
                try:
                    if re.match("^\\d{4}-\\d{2}-\\d{2}$", v):
                        dct[k] = Date.convert_to_date(v, original_format=Date.EN_ORIGINAL_FORMAT)
                    if re.match("^\\d{2}/\\d{2}/\\d{4}$", v):
                        dct[k] = Date.convert_to_date(v, original_format=Date.BR_ORIGINAL_FORMAT)
                except:
                    pass
        return dct

