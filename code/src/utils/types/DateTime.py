import datetime
import re
from typing import Optional

from pyparsing import basestring


class Date:

    BR_ORIGINAL_FORMAT = "%d/%m/%Y"
    EN_ORIGINAL_FORMAT = "%Y-%m-%d"

    @staticmethod
    def add_days(days: int):
        if days >= 0:
            return datetime.datetime.now() + datetime.timedelta(days=days)
        else:
            return datetime.datetime.now() - datetime.timedelta(days=(days * -1))

    @staticmethod
    def convert_to_date(date: str,
                        original_format: Optional[str] = None):
        if original_format is None:
            original_format = Date.BR_ORIGINAL_FORMAT
        return datetime.datetime.strptime(date, original_format)


class DateTime:

    @staticmethod
    def add_days(days: int):
        if days >= 0:
            return datetime.datetime.now() + datetime.timedelta(days=days)
        else:
            return datetime.datetime.now() - datetime.timedelta(days=(days * -1))

